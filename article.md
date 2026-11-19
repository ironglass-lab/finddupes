---
title: Як я боровся з дублями фото в архіві майстерні
permalink: /article.html
---

# Як я боровся з дублями фото в архіві майстерні — і написав для цього свій скрипт

🇺🇦 [Українська](#укр) (за замовчуванням) · [Русский](#рус) · 🇬🇧 [English](#eng)

---

<a id="укр"></a>
## 🇺🇦 Українська

За роки роботи з вітражами — а це з 1997 року — у мене накопичився величезний особистий
фотоархів: ескізи, процес збирання, готові вітражі, різні версії одних і тих самих кадрів для
каталогу, для Etsy, для сайту, для клієнтів. Фото копіювалися між папками під час
реорганізації архіву, дублювалися при бекапах, іноді одне й те саме фото опинялося в кількох
місцях під різними іменами — я перейменовував файли під різні потреби, а зрештою губився
рахунок, де оригінал, а де зайва копія.

У якийсь момент стало зрозуміло, що вручну перебирати десятки тисяч файлів нереально, а готові
програми для пошуку дублів або вимагали ставити щось незрозуміле з інтернету, або просто
видаляли файли без можливості відкотити — а втрачати архів за 25+ років роботи зовсім не
хотілося.

Оскільки з адмініструванням Linux і написанням скриптів я дружу давно (вся інфраструктура
офісу та майстерень — від саморобної сигналізації на ESP32 до VPN-сервера — у мене своя), вирішив не шукати
чуже рішення, а написати своє — просте, прозоре і безпечне.

### Як влаштований скрипт

`finddupes.py` — порівнює файли не за іменем (ім'я якраз те, що найчастіше змінювалося), а за
**вмістом**: рахує SHA-256 хеш кожного файлу-зображення. Якщо у двох файлів хеш збігається —
значить, це побайтово один і той самий файл, байдуже, як він називається і в якій підпапці
лежить.

Головне правило, яке я заклав з самого початку: **скрипт нічого не видаляє**. Знайдені зайві
копії переносяться в окрему папку `_duplicates/` — можна спокійно подивитися, що туди
потрапило, і тільки потім вирішити, видаляти чи ні. Для архіву, який збирався 25 років, це був
принциповий момент — помилка в автоматиці не повинна коштувати втрати фотографій.

Скрипт повністю на стандартній бібліотеці Python, без сторонніх залежностей — можна просто
завантажити і запустити.

### Код

Виклав на GitHub — [`finddupes.py`](https://github.com/ironglass-lab/finddupes): простий інструмент, який
вирішив мою власну проблему з архівом майстерні, можливо, знадобиться комусь ще з такою самою
задачею.

---
*Андрій Забегловський, майстерня вітражів Ironglass — [ironglass.com.ua](https://ironglass.com.ua)*

---

<a id="рус"></a>
## Русский

За годы работы с витражами — а это с 1997 года — у меня накопился огромный личный фотоархив:
эскизы, процесс сборки, готовые витражи, разные версии одних и тех же кадров для каталога,
для Etsy, для сайта, для клиентов. Фото копировались между папками при реорганизации архива,
дублировались при бэкапах, иногда одно и то же фото оказывалось в нескольких местах под
разными именами — я переименовывал файлы под разные нужды, а в итоге терялся счёт, где
оригинал, а где лишняя копия.

В какой-то момент стало понятно, что вручную перебирать десятки тысяч файлов нереально, а
готовые программы для поиска дублей либо требовали ставить что-то непонятное из интернета,
либо просто удаляли файлы без возможности откатить — а терять архив за 25+ лет работы совсем
не хотелось.

Поскольку с администрированием Linux и написанием скриптов я дружу давно (вся инфраструктура
офиса и мастерских — от самодельной сигнализации на ESP32 до VPN-сервера — у меня своя), решил не искать
чужое решение, а написать своё — простое, прозрачное и безопасное.

### Как устроен скрипт

`finddupes.py` — сравнивает файлы не по имени (имя как раз то, что чаще всего менялось), а по
**содержимому**: считает SHA-256 хеш каждого файла-изображения. Если у двух файлов хеш
совпадает — значит, это побайтово один и тот же файл, неважно, как он называется и в какой
подпапке лежит.

Главное правило, которое я заложил с самого начала: **скрипт ничего не удаляет**. Найденные
лишние копии переносятся в отдельную папку `_duplicates/` — можно спокойно посмотреть, что
туда попало, и только потом решить, удалять или нет. Для архива, который собирался 25 лет,
это был принципиальный момент — ошибка в автоматике не должна стоить потери фотографий.

Скрипт полностью на стандартной библиотеке Python, без сторонних зависимостей — можно просто
скачать и запустить.

### Код

Выложил на GitHub — [`finddupes.py`](https://github.com/ironglass-lab/finddupes): простой инструмент, который
решил мою собственную проблему с архивом мастерской, возможно, пригодится кому-то ещё с той же
задачей.

---
*Андрей Забегловский, мастерская витражей Ironglass — [ironglass.com.ua](https://ironglass.com.ua)*

---

<a id="eng"></a>
## 🇬🇧 English

Over the years of working with stained glass — since 1997 — I've built up a huge personal
photo archive: sketches, the assembly process, finished pieces, different versions of the
same shots for the catalog, for Etsy, for the website, for clients. Photos got copied
between folders while reorganizing the archive, duplicated during backups, and sometimes the
same photo ended up in several places under different names — I'd rename files for different
purposes, and eventually lost track of which one was the original and which was a leftover
copy.

At some point it became clear that going through tens of thousands of files by hand wasn't
realistic, and the ready-made duplicate finders out there either wanted me to install some
random piece of software, or would just delete files with no way to undo it — and losing a
25+ year archive was the last thing I wanted.

Since I've been comfortable with Linux administration and scripting for a long time (all the
infrastructure at the office and workshops — from a self-built ESP32 alarm system to a VPN server — is my own), I
decided not to look for someone else's solution, but to write my own: simple, transparent and
safe.

### How the script works

`finddupes.py` compares files not by name (the name was exactly what kept changing), but by
**content**: it computes a SHA-256 hash of every image file. If two files have the same hash,
they're byte-for-byte the same file, no matter what it's called or which subfolder it's in.

The main rule I built in from the start: **the script never deletes anything**. Duplicates it
finds are moved into a separate `_duplicates/` folder — you can calmly look through what ended
up there and only then decide whether to delete it. For an archive built up over 25 years,
that was a non-negotiable point — a mistake in the automation should never cost you your
photos.

The script is pure Python standard library, no third-party dependencies — just download it
and run it.

### The code

I put it up on GitHub — [`finddupes.py`](https://github.com/ironglass-lab/finddupes): a simple tool that solved my own
workshop-archive problem, and might be useful to someone else with the same one.

---
*Andrii Zabehlovskyi, Ironglass stained glass workshop — [ironglass.com.ua](https://ironglass.com.ua)*
