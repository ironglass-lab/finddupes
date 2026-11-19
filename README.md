# finddupes.py — пошук точних дублів фото за вмістом файлу

Скрипт рекурсивно сканує вказану папку (і всі підпапки), знаходить файли-зображення з
**однаковим вмістом** (порівняння за SHA-256 хешем, а не за іменем файлу), і переносить
зайві копії в окрему папку `_duplicates/` для перевірки — нічого не видаляє автоматично.

🇺🇦 [Українська](#укр) · [Русский](#рус) · 🇬🇧 [English](#eng)

### 📥 [Скачати finddupes.py](finddupes.py) &nbsp;|&nbsp; [Download finddupes.py](finddupes.py)

---

<a id="укр"></a>
## 🇺🇦 Українська

Скрипт написаний для [вітражної майстерні Ironglass](https://ironglass.com.ua/) — щоб навести
лад у власному фотоархіві готових робіт та процесу виготовлення.

### Що робить

- Рекурсивно обходить вказану папку та всі вкладені підпапки.
- Знаходить файли-зображення (`.jpg .jpeg .png .webp .gif .bmp .tif .tiff .heic .heif`).
- Рахує SHA-256 хеш **вмісту** кожного файлу — тобто знаходить дублі, навіть якщо файл
  перейменований або лежить в іншій підпапці. Два файли з різним вмістом (навіть дуже
  схожі фото — той самий кадр, інше стиснення чи розмір) дублями **не** вважаються.
- З кожної групи дублів залишає один файл як "оригінал" (той, що має найранішу дату
  зміни), решту переносить у `_duplicates/` (структура підпапок зберігається).
- Нічого не видаляє — лише переносить. Видаляти `_duplicates/` вручну, коли переконаєтесь,
  що все вірно.

### Вимоги

- Python 3 (жодних додаткових бібліотек ставити не потрібно — тільки стандартна бібліотека).
- Протестовано на Ubuntu 26.04; скрипту потрібна лише стандартна бібліотека Python 3, тож має
  працювати на будь-якій ОС з Python 3 — Windows/macOS/інші дистрибутиви Linux включно.

### Встановлення

Просто завантажте файл `finddupes.py` — встановлювати нічого не треба.

```bash
python3 finddupes.py --help
```

### Використання

```bash
# 1. Спочатку "сухий прогін" — подивитись, що буде знайдено, нічого не чіпаючи:
python3 finddupes.py /шлях/до/альбомів --dry-run

# 2. Коли переконались, що все вірно — перенести дублі насправді:
python3 finddupes.py /шлях/до/альбомів

# 3. Можна одразу зберегти звіт у CSV-файл:
python3 finddupes.py /шлях/до/альбомів --report dupes.csv

# 4. Можна задати іншу назву папки для дублів (за замовчуванням _duplicates):
python3 finddupes.py /шлях/до/альбомів --dupes-dir old_duplicates
```

### Параметри

| Параметр        | Опис                                                                 |
|-----------------|-----------------------------------------------------------------------|
| `root`          | Обов'язковий. Папка, яку скануємо (разом з усіма підпапками).         |
| `--dry-run`     | Лише показати, що буде знайдено/перенесено — нічого фактично не чіпає.|
| `--dupes-dir`   | Назва папки для дублів (створюється всередині `root`). За замовчуванням `_duplicates`. |
| `--report FILE` | Зберегти CSV-звіт (оригінал → дубль → куди перенесено → хеш) у вказаний файл. |

### Приклад виводу

```
Сканирую: /home/user/Photos
Проверено файлов: 842
Найдено групп дублей: 3, лишних копий: 5

Оригинал: /home/user/Photos/2023/event1/IMG_001.jpg
   дубль:  /home/user/Photos/backup/IMG_001_copy.jpg  ->  /home/user/Photos/_duplicates/backup/IMG_001_copy.jpg
...
Готово. Лишние копии перенесены в: /home/user/Photos/_duplicates
Файлы не удалены — можно проверить и удалить вручную, когда убедитесь, что всё верно.
```

### Безпека

Скрипт ніколи не видаляє файли самостійно — тільки переносить (`move`). Якщо помилково
запустити на неправильній папці, досить перенести файли з `_duplicates/` назад — нічого
не загублено.

---

<a id="рус"></a>
## Русский

Скрипт написан для [витражной мастерской Ironglass](https://ironglass.com.ua/) — чтобы навести
порядок в собственном фотоархиве готовых работ и процесса изготовления.

### Что делает

- Рекурсивно обходит указанную папку и все вложенные подпапки.
- Находит файлы-изображения (`.jpg .jpeg .png .webp .gif .bmp .tif .tiff .heic .heif`).
- Считает SHA-256 хеш **содержимого** каждого файла — то есть находит дубли, даже если
  файл переименован или лежит в другой подпапке. Два файла с разным содержимым (даже
  очень похожие фото — тот же кадр, но другое сжатие или размер) дублями **не**
  считаются.
- Из каждой группы дублей оставляет один файл как "оригинал" (тот, у которого самая
  ранняя дата изменения), остальные переносит в `_duplicates/` (структура подпапок
  сохраняется).
- Ничего не удаляет — только переносит. Удалять `_duplicates/` вручную, когда убедитесь,
  что всё верно.

### Требования

- Python 3 (никаких дополнительных библиотек ставить не нужно — только стандартная
  библиотека).
- Протестировано на Ubuntu 26.04; скрипту нужна только стандартная библиотека Python 3,
  поэтому должен работать на любой ОС с Python 3 — Windows/macOS/другие дистрибутивы Linux
  включая.

### Установка

Просто скачайте файл `finddupes.py` — устанавливать ничего не нужно.

```bash
python3 finddupes.py --help
```

### Использование

```bash
# 1. Сначала "сухой прогон" — посмотреть, что будет найдено, ничего не трогая:
python3 finddupes.py /путь/к/альбомам --dry-run

# 2. Когда убедились, что всё верно — перенести дубли по-настоящему:
python3 finddupes.py /путь/к/альбомам

# 3. Можно сразу сохранить отчёт в CSV-файл:
python3 finddupes.py /путь/к/альбомам --report dupes.csv

# 4. Можно задать другое имя папки для дублей (по умолчанию _duplicates):
python3 finddupes.py /путь/к/альбомам --dupes-dir old_duplicates
```

### Параметры

| Параметр        | Описание                                                               |
|-----------------|-------------------------------------------------------------------------|
| `root`          | Обязательный. Папка, которую сканируем (вместе со всеми подпапками).    |
| `--dry-run`     | Только показать, что будет найдено/перенесено — ничего фактически не трогает. |
| `--dupes-dir`   | Имя папки для дублей (создаётся внутри `root`). По умолчанию `_duplicates`. |
| `--report FILE` | Сохранить CSV-отчёт (оригинал → дубль → куда перенесено → хеш) в указанный файл. |

### Пример вывода

```
Сканирую: /home/user/Photos
Проверено файлов: 842
Найдено групп дублей: 3, лишних копий: 5

Оригинал: /home/user/Photos/2023/event1/IMG_001.jpg
   дубль:  /home/user/Photos/backup/IMG_001_copy.jpg  ->  /home/user/Photos/_duplicates/backup/IMG_001_copy.jpg
...
Готово. Лишние копии перенесены в: /home/user/Photos/_duplicates
Файлы не удалены — можно проверить и удалить вручную, когда убедитесь, что всё верно.
```

### Безопасность

Скрипт никогда не удаляет файлы самостоятельно — только переносит (`move`). Если
случайно запустить не на той папке, достаточно перенести файлы из `_duplicates/`
обратно — ничего не потеряно.

---

<a id="eng"></a>
## 🇬🇧 English

The script was written for the [Ironglass stained glass workshop](https://ironglass.com.ua/) —
to tidy up a personal photo archive of finished pieces and the production process.

### What it does

- Recursively walks the given folder and all its subfolders.
- Finds image files (`.jpg .jpeg .png .webp .gif .bmp .tif .tiff .heic .heif`).
- Computes a SHA-256 hash of each file's **content** — so it finds duplicates even if a
  file was renamed or lives in a different subfolder. Two files with different content
  (even a very similar photo — the same shot re-exported at a different size or
  compression) are **not** treated as duplicates.
- From each group of duplicates, keeps one file as the "original" (the one with the
  earliest modification date) and moves the rest into `_duplicates/` (subfolder
  structure is preserved).
- Nothing is ever deleted — only moved. Delete `_duplicates/` yourself once you've
  confirmed everything is correct.

### Requirements

- Python 3 (no extra packages needed — standard library only).
- Tested on Ubuntu 26.04; the script only needs the Python 3 standard library, so it should
  work on any OS with Python 3 — Windows/macOS/other Linux distributions included.

### Installation

Just download `finddupes.py` — nothing to install.

```bash
python3 finddupes.py --help
```

### Usage

```bash
# 1. Dry run first — see what would be found without touching anything:
python3 finddupes.py /path/to/albums --dry-run

# 2. Once you're happy with the result, actually move the duplicates:
python3 finddupes.py /path/to/albums

# 3. Save a CSV report at the same time:
python3 finddupes.py /path/to/albums --report dupes.csv

# 4. Use a custom folder name for duplicates (default is _duplicates):
python3 finddupes.py /path/to/albums --dupes-dir old_duplicates
```

### Options

| Option          | Description                                                            |
|-----------------|-------------------------------------------------------------------------|
| `root`          | Required. The folder to scan (including all subfolders).               |
| `--dry-run`     | Only show what would be found/moved — doesn't touch any files.         |
| `--dupes-dir`   | Name of the folder duplicates are moved into (created inside `root`). Defaults to `_duplicates`. |
| `--report FILE` | Save a CSV report (original → duplicate → moved-to path → hash) to the given file. |

### Example output

```
Сканирую: /home/user/Photos
Проверено файлов: 842
Найдено групп дублей: 3, лишних копий: 5

Оригинал: /home/user/Photos/2023/event1/IMG_001.jpg
   дубль:  /home/user/Photos/backup/IMG_001_copy.jpg  ->  /home/user/Photos/_duplicates/backup/IMG_001_copy.jpg
...
Готово. Лишние копии перенесены в: /home/user/Photos/_duplicates
Файлы не удалены — можно проверить и удалить вручную, когда убедитесь, что всё верно.
```

### Safety

The script never deletes files on its own — it only moves them. If you accidentally run
it on the wrong folder, just move the files back out of `_duplicates/` — nothing is lost.

---

Author: Andrii Zabehlovskyi — [Ironglass stained glass workshop](https://ironglass.com.ua/)
