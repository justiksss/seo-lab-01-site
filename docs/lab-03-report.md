# ЗВІТ до лабораторної роботи №3

**Дисципліна:** Пошукова оптимізація, технології та сервіси веб-аналітики  
**Тема:** Технічна оптимізація вебсайту

**Виконав:**  
[Прізвище Ім'я По батькові],  
студент групи [група] факультету інформаційних технологій і математики

**Перевірив:**  
Ройко Олександр Юрійович, кандидат технічних наук, доцент

**Місто, рік:** Луцьк 2026

---

## ЗМІСТ

1. [Вступ](#вступ)
2. [Розділ 1. Базовий аудит сайту](#розділ-1-базовий-аудит-сайту)
3. [Розділ 2. Оптимізація зображень](#розділ-2-оптимізація-зображень)
4. [Розділ 3. Lazy loading](#розділ-3-lazy-loading)
5. [Розділ 4. Файл robots.txt](#розділ-4-файл-robotstxt)
6. [Розділ 5. XML Sitemap та Google Search Console](#розділ-5-xml-sitemap-та-google-search-console)
7. [Розділ 6. Порівняльний аналіз «до/після»](#розділ-6-порівняльний-аналіз-допісля)
8. [Висновки](#висновки)

---

## Вступ

**Тема.** Технічна оптимізація вебсайту.

**Мета.** Провести технічний аудит через PageSpeed Insights, оптимізувати зображення (стиснення, WebP), налаштувати lazy loading, оформити `robots.txt` і XML Sitemap, надіслати карту в Google Search Console, порівняти Core Web Vitals до та після змін.

**Завдання** (згідно з [lab-03](https://github.com/olroi421/course-seo/blob/main/labs/lab-03.md)):

1. Базове тестування PageSpeed Insights (метрики до оптимізації).
2. Оптимізація зображень: стиснення та WebP.
3. Lazy loading для медіа нижче першого екрана.
4. `robots.txt` з коректними директивами.
5. XML Sitemap і надсилання в GSC.
6. Повторне тестування та порівняння метрик.
7. Звіт із документуванням покращень.

**Об'єкт дослідження.** Навчальний статичний сайт **SEO Lab 01** для лабораторних з технічного SEO (аудит, метадані, Core Web Vitals).

- **URL:** https://justiksss.github.io/seo-lab-01-site/
- **Тип:** навчальний багатосторінковий статичний сайт (не комерційний).
- **Технології:** HTML, CSS; хостинг GitHub Pages.
- **Репозиторій:** https://github.com/justiksss/seo-lab-01-site

---

## Розділ 1. Базовий аудит сайту

Перед оптимізацією перевірено головну сторінку в [PageSpeed Insights](https://pagespeed.web.dev/). Саме вона містить hero-зображення та галерею після впровадження Lab 03 (для «до» знімай стан **без** WebP/галереї — див. `docs/lab-03-screenshots.md`).

### Таблиця 1.1. Базові метрики Core Web Vitals (ДО оптимізації)

| Метрика | Mobile (до) | Desktop (до) | Норма |
|---------|-------------|--------------|-------|
| Performance Score | _заповнити_ | _заповнити_ | 90+ |
| LCP | _заповнити_ | _заповнити_ | ≤ 2,5 с |
| INP | _заповнити_ | _заповнити_ | ≤ 200 мс |
| CLS | _заповнити_ | _заповнити_ | ≤ 0,1 |
| FCP | _заповнити_ | _заповнити_ | ≤ 1,8 с |
| TTFB | _заповнити_ | _заповнити_ | ≤ 800 мс |

**[ВСТАВИТИ СКРІНШОТ: PageSpeed Insights — вкладка Mobile, блок Core Web Vitals і Performance Score]**

*Рис. 1.1. Результати PageSpeed Insights (Mobile) до оптимізації*

**Як зробити скріншот:** відкрий https://pagespeed.web.dev/ → встав `https://justiksss.github.io/seo-lab-01-site/` → дочекайся аналізу → вкладка **Mobile** → `Cmd+Shift+4` (macOS) або `Win+Shift+S` (Windows) → збережи PNG у папку `screenshots/lab03/`.

**[ВСТАВИТИ СКРІНШОТ: PageSpeed Insights — вкладка Desktop]**

*Рис. 1.2. Результати PageSpeed Insights (Desktop) до оптимізації*

### Виявлені рекомендації (типові для сайту з важкими JPEG)

- **Serve images in next-gen formats** — потрібен WebP/AVIF.
- **Properly size images** — розміри файлів і відображення.
- **Defer offscreen images** — lazy loading для галереї.
- **Image elements do not have explicit width and height** — ризик зміщення макету (CLS).

**[ВСТАВИТИ СКРІНШОТ: розділ Opportunities / Diagnostics з рекомендаціями про зображення]**

*Рис. 1.3. Рекомендації PageSpeed щодо зображень (до оптимізації)*

---

## Розділ 2. Оптимізація зображень

### 2.1. Інвентаризація

| Файл | Сторінка | Формат до | Розмір до | alt | width/height |
|------|----------|-----------|-----------|-----|--------------|
| hero.jpg | index.html (hero) | JPEG | ~78 КБ | так | 1200×600 |
| gallery-1.jpg | index.html (галерея) | JPEG | ~93 КБ | так | 800×600 |
| gallery-2.jpg | index.html | JPEG | ~93 КБ | так | 800×600 |
| gallery-3.jpg | index.html, services/web.html | JPEG | ~22 КБ | так | 800×600 |

Повна таблиця з байтами: `docs/lab-03-image-inventory.md`.

### 2.2. Стиснення та WebP (Squoosh)

Для кожного JPEG:

1. Відкрий https://squoosh.app/
2. Перетягни файл з `assets/img/lab03/` (наприклад `hero.jpg`).
3. Справа обери **WebP**, якість **80–85%**.
4. Порівняй повзунком якість/розмір.
5. Завантаж `.webp` (у репозиторії вже є версії після `cwebp -q 82`).

### Таблиця 2.1. Порівняння «до / після»

| Файл | Формат (до → після) | Розмір до | Розмір після | Зменшення |
|------|---------------------|-----------|--------------|-----------|
| hero | JPEG → WebP | 78 КБ | 61 КБ* | ~22% |
| gallery-1 | JPEG → WebP | 93 КБ | 85 КБ* | ~8% |
| gallery-2 | JPEG → WebP | 93 КБ | 90 КБ* | ~3% |
| gallery-3 | JPEG → WebP | 22 КБ | 13 КБ* | ~40% |

\*Після `cwebp`; у PDF можна вказати менші значення з Squoosh.

**[ВСТАВИТИ СКРІНШОТ: Squoosh — hero.jpg, формат WebP, порівняння розміру]**

*Рис. 2.1. Стиснення в Squoosh*

### 2.3. Оновлення HTML (`<picture>` + fallback)

Головний банер (без lazy loading — впливає на LCP):

```html
<picture>
  <source srcset="assets/img/lab03/hero.webp" type="image/webp">
  <img class="hero-image"
       src="assets/img/lab03/hero.jpg"
       alt="Ілюстрація технічного SEO-аудиту: аналітика та оптимізація сайту"
       width="1200"
       height="600">
</picture>
```

Галерея (з `loading="lazy"`):

```html
<picture>
  <source srcset="assets/img/lab03/gallery-1.webp" type="image/webp">
  <img src="assets/img/lab03/gallery-1.jpg"
       alt="Скріншот звіту PageSpeed Insights для мобільної версії"
       width="800"
       height="600"
       loading="lazy">
</picture>
```

Код у репозиторії: `index.html`, `services/web.html`.

**[ВСТАВИТИ СКРІНШОТ: головна сторінка в браузері після деплою — hero + галерея]**

*Рис. 2.2. Сторінка після впровадження WebP*

---

## Розділ 3. Lazy loading

**Правило:** hero завантажується одразу; зображення галереї та на `services/web.html` — з `loading="lazy"`.

| Зображення | Сторінка | lazy loading |
|------------|----------|--------------|
| hero.jpg / hero.webp | index.html | **ні** (above the fold, LCP) |
| gallery-1, gallery-2, gallery-3 | index.html | **так** |
| gallery-3 | services/web.html | **так** |

**Обґрунтування:** відкладене завантаження hero погіршило б LCP; галерея нижче першого екрана — кандидати на lazy loading.

### Перевірка в DevTools

1. Відкрий https://justiksss.github.io/seo-lab-01-site/
2. `F12` → **Network** → фільтр **Img**
3. `Cmd+Shift+R` (hard reload)
4. Без прокрутки — лише hero (+ дрібні іконки, якщо є)
5. Прокрути до галереї — з’являться запити `gallery-*.webp`

**[ВСТАВИТИ СКРІНШОТ: Network після reload без прокрутки]**

*Рис. 3.1. Завантаження лише hero*

**[ВСТАВИТИ СКРІНШОТ: Network після прокрутки — gallery]**

*Рис. 3.2. Відкладене завантаження галереї*

---

## Розділ 4. Файл robots.txt

**URL:** https://justiksss.github.io/seo-lab-01-site/robots.txt

### Повний вміст

```
User-agent: *
Disallow: /redirect-a.html
Disallow: /redirect-b.html
Disallow: /redirect-c.html
Disallow: /duplicate-title-1.html
Disallow: /duplicate-title-2.html
Allow: /

Sitemap: https://justiksss.github.io/seo-lab-01-site/sitemap.xml
```

### Пояснення директив

| Директива | Призначення |
|-----------|-------------|
| `User-agent: *` | Правила для всіх ботів |
| `Disallow: /redirect-*.html` | Не витрачати краулінговий бюджет на навчальні ланцюги редиректів (Lab 01) |
| `Disallow: /duplicate-title-*.html` | Технічні сторінки з дубльованими title (Lab 01) |
| `Allow: /` | Решта сторінок доступні для індексації |
| `Sitemap:` | Пряме посилання на XML Sitemap |

**[ВСТАВИТИ СКРІНШОТ: robots.txt у браузері]**

**[ВСТАВИТИ СКРІНШОТ: GSC → Settings → robots.txt → Open report (без критичних помилок)]**

*Рис. 4.1. Перевірка robots.txt у Google Search Console*

---

## Розділ 5. XML Sitemap та Google Search Console

**URL Sitemap:** https://justiksss.github.io/seo-lab-01-site/sitemap.xml

У карту включено пріоритетні навчальні сторінки (головна, about, contact, faq, glossary, services, blog). Сторінки з `Disallow` у robots.txt навмисно **не** додані до sitemap.

Приклад запису:

```xml
<url>
  <loc>https://justiksss.github.io/seo-lab-01-site/</loc>
  <lastmod>2026-05-26</lastmod>
  <changefreq>weekly</changefreq>
  <priority>1.0</priority>
</url>
```

### Надсилання в GSC

1. [Google Search Console](https://search.google.com/search-console) → ресурс `https://justiksss.github.io/seo-lab-01-site/`
2. Меню **Sitemaps** (Файли Sitemap)
3. Поле «Додати нову карту сайту» → `sitemap.xml` → **Надіслати**
4. Дочекайся статусу Success або Pending

**[ВСТАВИТИ СКРІНШОТ: вміст sitemap.xml у браузері]**

**[ВСТАВИТИ СКРІНШОТ: GSC → Sitemaps — статус sitemap.xml]**

*Рис. 5.1. Надсилання Sitemap до Google Search Console*

Якщо статус **Pending** / «Не вдалося прочитати» для нового GitHub Pages:

- Перевір **URL Inspection** → Test Live URL для `.../sitemap.xml`
- Дочекайся планового обходу (1–7 днів)

**[ВСТАВИТИ СКРІНШОТ (за потреби): URL Inspection — URL available to Google]**

---

## Розділ 6. Порівняльний аналіз «до/після»

Після `git push` і оновлення GitHub Pages повтори PageSpeed для того самого URL.

### Таблиця 6.1. Метрики до та після

| Метрика | Mobile до | Mobile після | Desktop до | Desktop після |
|---------|-----------|--------------|------------|---------------|
| Performance Score | | | | |
| LCP | | | | |
| INP | | | | |
| CLS | | | | |
| FCP | | | | |

**Відсоток покращення (приклад для LCP Mobile):**  
`((LCP_до - LCP_після) / LCP_до) × 100%`

**[ВСТАВИТИ СКРІНШОТ: PageSpeed Mobile після оптимізації]**

**[ВСТАВИТИ СКРІНШОТ: PageSpeed Desktop після оптимізації]**

### Залишкові рекомендації (шаблон для аналізу)

| Рекомендація | Статус після Lab 03 | Чому могла залишитися |
|--------------|---------------------|------------------------|
| Next-gen formats | частково вирішено | WebP через `<picture>` |
| Defer offscreen images | вирішено | `loading="lazy"` на галереї |
| Render-blocking CSS | може залишатися | один файл `style.css` без Critical CSS |
| Мало трафіку для Field Data | — | CWV у полі оновлюються з затримкою |

Для оцінки щойно зроблених змін орієнтуйся на **Lab Data** у PageSpeed, а не лише на Field Data.

---

## Висновки

У межах лабораторної роботи №3 на навчальному сайті SEO Lab виконано технічний аудит швидкості, оптимізовано зображення (JPEG + WebP через `<picture>`), налаштовано lazy loading для контенту нижче першого екрана, оновлено `robots.txt` і `sitemap.xml`, карту сайту надіслано до Google Search Console.

Найбільший практичний ефект для LCP дає оптимізація hero-зображення та відмова від одночасного завантаження всіх картинок галереї. Атрибути `width` і `height` допомагають утримувати CLS у прийнятних межах.

Подальші кроки: мініфікація CSS, preload для hero WebP, моніторинг Core Web Vitals у GSC (звіт **Experience → Core Web Vitals**).

---

## Контрольні запитання (короткі відповіді для захисту)

1. **Core Web Vitals** — LCP (швидкість найбільшого елемента, ≤2,5 с), INP (реакція на дію, ≤200 мс), CLS (стабільність макету, ≤0,1).
2. **WebP** — менший розмір при подібній якості; мінус — потрібен fallback для старих клієнтів (`<picture>`).
3. **Lazy loading** — не застосовувати до LCP-елемента (hero above the fold).
4. **robots.txt** — інструкції для ботів; `Disallow` забороняє шлях, `Allow` дозволяє після широкої заборони.
5. **Sitemap** — прискорює знаходження URL, важлива для нових/слабо пов’язаних сторінок.
6. **`width`/`height`** — резервують місце в макеті, зменшують CLS.
7. **Field vs Lab Data** — після змін орієнтуйся на Lab Data; Field оновлюється з затримкою через реальних користувачів.

---

*Детальні інструкції до скріншотів: `docs/lab-03-screenshots.md`. Шаблон оформлення PDF — Google Drive «lab3-seo- yudin».*
