# Lab 03 — як зробити скріншоти для PDF-звіту

Сайт: **https://justiksss.github.io/seo-lab-01-site/**  
Головна для PageSpeed: **https://justiksss.github.io/seo-lab-01-site/** (або `index.html`)

> **Важливо:** скріни «ДО» знімай **до** `git push` з оптимізацією Lab 03 (коміт без WebP/gallery) або збережи знімки з локального сервера на старому коміті.

---

## Розділ 1. Базовий аудит (ДО)

| # | Що знімати | Як |
|---|------------|-----|
| 1.1 | PageSpeed Insights — **Mobile**, оцінка + CWV | [pagespeed.web.dev](https://pagespeed.web.dev/) → встав URL → вкладка **Mobile** → скрін усього блоку з Performance, LCP, INP, CLS, FCP, TTFB |
| 1.2 | PageSpeed Insights — **Desktop** | Та сама сторінка → вкладка **Desktop** → скрін |
| 1.3 | Opportunities / Diagnostics (зображення) | Прокрути вниз → розділи з рекомендаціями про images → скрін 1–2 блоків |

**macOS:** `Cmd + Shift + 4` → виділи область. **Windows:** `Win + Shift + S`.

---

## Розділ 2. Оптимізація зображень

| # | Що знімати | Як |
|---|------------|-----|
| 2.1 | Squoosh | [squoosh.app](https://squoosh.app/) → завантаж `assets/img/lab03/hero.jpg` → формат **WebP**, якість **82** → скрін порівняння розміру до/після |
| 2.2 | Сторінка в браузері (опційно) | Відкрий головну після деплою — видно hero + галерею |

---

## Розділ 3. Lazy loading

| # | Що знімати | Як |
|---|------------|-----|
| 3.1 | DevTools → Network | Відкрий головну → `F12` → **Network** → фільтр **Img** → `Cmd+Shift+R` (hard reload) → скрін: видно лише hero (і дрібні ресурси), без gallery |
| 3.2 | Після прокрутки | Прокрути до галереї → у Network з’являться `gallery-*.webp` / `.jpg` → другий скрін |

---

## Розділ 4. robots.txt

| # | Що знімати | Як |
|---|------------|-----|
| 4.1 | Файл у браузері | Відкрий https://justiksss.github.io/seo-lab-01-site/robots.txt → скрін вмісту |
| 4.2 | Google Search Console | [search.google.com/search-console](https://search.google.com/search-console) → ваш ресурс → **Settings** → **robots.txt** → **Open report** → скрін без помилок |

---

## Розділ 5. Sitemap + GSC

| # | Що знімати | Як |
|---|------------|-----|
| 5.1 | sitemap.xml у браузері | https://justiksss.github.io/seo-lab-01-site/sitemap.xml |
| 5.2 | GSC → Sitemaps | Ліве меню **Sitemaps** → поле «Add a new sitemap» → введи `sitemap.xml` → **Submit** → скрін статусу (Success / Pending) |
| 5.3 | (якщо Pending) URL Inspection | Верхній рядок GSC → URL sitemap → **Test Live URL** → скрін «URL is available to Google» |

---

## Розділ 6. Після оптимізації

| # | Що знімати | Як |
|---|------------|-----|
| 6.1 | PageSpeed Mobile (після) | Повтори крок 1.1 після деплою Lab 03 |
| 6.2 | PageSpeed Desktop (після) | Повтори крок 1.2 |

Заповни таблицю в `docs/lab-03-report.md` (розділ 6).

---

## Експорт у PDF

1. Скопіюй текст із `docs/lab-03-report.md` у Google Docs / Word (шаблон як у `lab3-seo- yudin`).
2. Встав скріни на місця `[ВСТАВИТИ СКРІНШОТ: …]`.
3. Заміни `[Прізвище Ім'я По батькові]` та `[група]` на свої дані.
4. **Файл → Завантажити → PDF**.
