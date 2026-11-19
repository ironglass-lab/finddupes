#!/usr/bin/env python3
"""
finddupes.py — пошук точних дублів фото (за вмістом файлу, SHA-256)
у вказаній папці та всіх її підпапках.

Порівнює файли за хешем вмісту, а не за іменем — знаходить дублі,
навіть якщо файл перейменовано або скопійовано в іншу підпапку.
Зайві копії не видаляються, а переносяться в окрему папку (_duplicates/
за замовчуванням) для ручної перевірки — так само, як у find_unused_images.sh.

Використання:
    python3 finddupes.py /шлях/до/альбомів
    python3 finddupes.py /шлях/до/альбомів --dry-run
    python3 finddupes.py /шлях/до/альбомів --dupes-dir _duplicates --report report.csv

Автор: Андрій Забегловський (Ironglass) — https://ironglass.com.ua
"""

import argparse
import csv
import hashlib
import os
import shutil
import sys
from collections import defaultdict
from pathlib import Path

# Розширення файлів, які вважаємо зображеннями
IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp",
    ".tif", ".tiff", ".heic", ".heif",
}


def iter_image_files(root: Path, exclude_dirs):
    """Рекурсивно обходить root і повертає шляхи до всіх файлів-зображень,
    пропускаючи папки з exclude_dirs (наприклад, саму папку з дублями)."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if Path(dirpath, d).resolve() not in exclude_dirs
        ]
        for name in filenames:
            p = Path(dirpath, name)
            if p.suffix.lower() in IMAGE_EXTENSIONS:
                yield p


def file_hash(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Рахує SHA-256 хеш вмісту файлу, читаючи його частинами
    (щоб не завантажувати у пам'ять великі файли цілком)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def pick_original(paths):
    """Оригіналом вважаємо файл із найранішою датою зміни;
    при рівності — у кого шлях коротший / алфавітно перший."""
    return sorted(paths, key=lambda p: (p.stat().st_mtime, len(str(p)), str(p)))[0]


def unique_dest(dupes_dir: Path, original_root: Path, src: Path) -> Path:
    """Формує шлях призначення всередині dupes_dir, зберігаючи відносну
    структуру підпапок з original_root, і уникає перезапису, якщо файл
    з такою ж назвою там вже є (додає суфікс __dupN)."""
    try:
        rel = src.relative_to(original_root)
    except ValueError:
        rel = Path(src.name)
    dest = dupes_dir / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        return dest
    stem, suf = dest.stem, dest.suffix
    i = 1
    while True:
        candidate = dest.with_name(f"{stem}__dup{i}{suf}")
        if not candidate.exists():
            return candidate
        i += 1


def main():
    ap = argparse.ArgumentParser(
        description="Пошук точних дублів фото за вмістом файлу (SHA-256)."
    )
    ap.add_argument(
        "root",
        help="Папка з фото/альбомами для перевірки (шукає рекурсивно у всіх підпапках)",
    )
    ap.add_argument(
        "--dupes-dir",
        default="_duplicates",
        help="Назва папки для перенесення дублів (за замовчуванням: _duplicates, створюється всередині root)",
    )
    ap.add_argument(
        "--report",
        default=None,
        help="Шлях до CSV-файлу зі звітом (за замовчуванням звіт виводиться лише в консоль)",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Лише показати, що було б зроблено, нічого не переносити",
    )
    args = ap.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        print(f"Помилка: папку не знайдено: {root}", file=sys.stderr)
        sys.exit(1)

    dupes_dir = (root / args.dupes_dir).resolve()
    exclude_dirs = {dupes_dir}

    print(f"Скануюю: {root}")
    hashes = defaultdict(list)
    count = 0
    for path in iter_image_files(root, exclude_dirs=exclude_dirs):
        try:
            h = file_hash(path)
        except OSError as e:
            print(f"  пропущено (не читається): {path} ({e})")
            continue
        hashes[h].append(path)
        count += 1

    print(f"Перевірено файлів: {count}")

    # Залишаємо лише групи, де більше одного файлу з однаковим хешем — це і є дублі
    groups = {h: paths for h, paths in hashes.items() if len(paths) > 1}
    if not groups:
        print("Точних дублів не знайдено.")
        return

    total_dupes = sum(len(paths) - 1 for paths in groups.values())
    print(f"Знайдено груп дублів: {len(groups)}, зайвих копій: {total_dupes}")
    print()

    report_rows = []
    for h, paths in groups.items():
        original = pick_original(paths)
        others = [p for p in paths if p != original]
        print(f"Оригінал: {original}")
        for dup in others:
            if args.dry_run:
                dest = "(не перенесено — dry-run)"
            else:
                dest_path = unique_dest(dupes_dir, root, dup)
                shutil.move(str(dup), str(dest_path))
                dest = str(dest_path)
            print(f"   дубль:  {dup}  ->  {dest}")
            report_rows.append(
                {
                    "original": str(original),
                    "duplicate": str(dup),
                    "moved_to": dest,
                    "sha256": h,
                }
            )
        print()

    if args.report:
        with open(args.report, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=["original", "duplicate", "moved_to", "sha256"]
            )
            writer.writeheader()
            writer.writerows(report_rows)
        print(f"Звіт збережено: {args.report}")

    if args.dry_run:
        print(
            "Це був dry-run — нічого не перенесено. "
            f"Запустіть без --dry-run, щоб перенести дублі в {dupes_dir}"
        )
    else:
        print(f"Готово. Зайві копії перенесено в: {dupes_dir}")
        print("Файли не видалені — можна перевірити і видалити вручну, коли переконаєтесь, що все вірно.")


if __name__ == "__main__":
    main()
