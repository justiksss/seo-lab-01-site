# Lab 02 — де робити скріншоти для PDF-звіту

## Розділ 1. Аудит метаданих (ДО)

| # | Що знімати | Як |
|---|------------|-----|
| 1.1 | META SEO Inspector на **головній** (старий стан) | Якщо вже запушено Lab 02 — використай таблицю `lab-02-audit-before.md` + 1–2 скріни з **локального** сервера на старому коміті, або опиши «до» з таблиці |
| 1.2 | Inspector на **page-no-title.html** | Показати відсутній/проблемний title |
| 1.3 | Inspector на **duplicate-title-1** і **-2** | Дубль title |
| 1.4 | Inspector на **blog/post-1** | Короткий description |

Мінімум: **4 скріни «до»** або таблиця + 2 скріни проблемних сторінок.

---

## Розділ 2. Метадані (ПІСЛЯ)

Після `git push` (коли сайт оновився на GitHub Pages):

| # | URL | Скрін Inspector |
|---|-----|-----------------|
| 2.1 | `/index.html` | Новий title + description (довжини ~50–60 / ~150) |
| 2.2 | `/faq.html` | |
| 2.3 | `/blog/post-1.html` | |
| 2.4 | `/services/seo.html` | |
| 2.5 | `/page-no-title.html` | Title з’явився |

Мінімум: **5 скрінів «після»**.

---

## Розділ 3. Structured data

| # | Інструмент | URL | Скрін |
|---|------------|-----|-------|
| 3.1 | [Rich Results Test](https://search.google.com/test/rich-results) | `.../faq.html` | Статус **Valid**, тип **FAQPage** |
| 3.2 | Rich Results Test | `.../blog/post-1.html` | Статус **Valid**, тип **Article** |
| 3.3 | (опційно) [validator.schema.org](https://validator.schema.org/) | той самий URL | Без критичних помилок |

Мінімум: **2 скріни** Rich Results (зелений Valid).

---

## Розділ 4. Internal linking

| # | Що знімати |
|---|------------|
| 4.1 | Фрагмент тексту на **index.html** у браузері — видно 3+ контекстних посилання в абзаці |
| 4.2 | **about.html** або **services/seo.html** — аналогічно |
| 4.3 | (опційно) Screaming Frog → Internal links export або схема «до/після» вручну в draw.io |

Мінімум: **2 скріни** сторінок з новими посиланнями в `<main>`.

---

## Розділ 5–6. Звіт

Таблиці скопіюй з:
- `docs/lab-02-audit-before.md`
- `docs/lab-02-audit-after.md`

Висновки: 5–6 речень (on-page, Schema, перелінковка).
