#!/usr/bin/env python3
"""Оновлення Google Doc lab3-seo- yudin під проєкт seo-lab-01-site (replaceAllText)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

DOC_ID = "1PkL_Me6v3cGCyLplrk7Y18ZKu3RjjQ3e-d1BrFVtjsg"
CREDS_PATH = Path.home() / ".config/mcp-gdrive/.gdrive-write-credentials.json"

# Порядок: від довших/специфічніших рядків до коротших
REPLACEMENTS: list[tuple[str, str]] = [
    (
        "Юдін Олексій Сергійович",
        "[Прізвище Ім'я По батькові]",
    ),
    (
        "Об'єкт дослідження. Мій навчальний вебсайт інтернет-магазину вина «Nice Wine», розроблений на базі статичного HTML/CSS/JS шаблону та розміщений на безкоштовному хостингу GitHub Pages.",
        "Об'єкт дослідження. Навчальний статичний сайт SEO Lab 01 для лабораторних з технічного SEO (аудит, метадані, Core Web Vitals), опублікований на GitHub Pages (репозиторій justiksss/seo-lab-01-site).",
    ),
    (
        "Для виконання цієї лабораторної роботи я використовую свій навчальний проєкт  інтернет-магазин вина «Nice Wine ».",
        "Для виконання лабораторної роботи використовую навчальний проєкт SEO Lab 01 — тестовий сайт для практики технічного SEO.",
    ),
    (
        "URL сайту: https://makss-gil.github.io/learn-seo-hilitukha/",
        "URL сайту: https://justiksss.github.io/seo-lab-01-site/",
    ),
    (
        "Тип сайту: E-commerce (каталог товарів, блог).",
        "Тип сайту: навчальний багатосторінковий статичний сайт (лабораторні Lab 01–03).",
    ),
    (
        "Технології: Статичний сайт на чистому HTML, CSS та JavaScript. Хостинг — GitHub Pages.",
        "Технології: HTML, CSS; хостинг GitHub Pages; репозиторій https://github.com/justiksss/seo-lab-01-site.",
    ),
    (
        "вона містить найбільше графічних елементів (банери, прев'ю товарів) і є найважливішою для користувачів.",
        "вона містить hero-зображення та галерею (після Lab 03) і є основною для перевірки PageSpeed.",
    ),
    (
        "Рис 1.1. Результати PageSpeed Insights для мобільних пристроїв до оптимізації",
        "Рис. 1.1. Результати PageSpeed Insights для мобільних пристроїв до оптимізації\n\n"
        "▶ Скріншот: відкрити https://pagespeed.web.dev/ → вставити URL https://justiksss.github.io/seo-lab-01-site/ "
        "→ вкладка Mobile → зняти екран (macOS: Cmd+Shift+4). Вставити зображення нижче цього рядка.",
    ),
    (
        "Рис. 1.2. Результати PageSpeed Insights для десктопу до оптимізації",
        "Рис. 1.2. Результати PageSpeed Insights для десктопу до оптимізації\n\n"
        "▶ Скріншот: та сама сторінка PageSpeed → вкладка Desktop → вставити зображення тут.",
    ),
    (
        "Аналіз показав, що головна проблема мого сайту — це занадто великі фотографії. Вони важили по 5-6 мегабайт, через що сторінка довго вантажилася. Тому другим кроком я зайнявся їх оптимізацією.\nДля цього я використав безкоштовний онлайн-інструмент Squoosh. Я по черзі завантажив туди всі важкі зображення з виноградниками та вином, які використовував на сайті (в основному це фото з Unsplash), і конвертував їх зі старого формату JPEG у сучасний формат WebP. Завдяки цьому розмір файлів зменшився більше ніж на 90%, при цьому візуальна якість картинки для користувача зовсім не постраждала.",
        "Аналіз показав, що значна частина ваги сторінки — зображення в каталозі assets/img/lab03/. Другим кроком виконано оптимізацію через Squoosh (якість WebP 80–85%) та утиліту cwebp у репозиторії. Файли hero.jpg, gallery-1..3.jpg конвертовано у WebP; для браузерів без підтримки WebP залишено JPEG fallback у тегу <picture>.",
    ),
    (
        "alexander-ugolkov-TkGI3Mkdurk-unsplash\nJPEG -> WebP\n2.3 MB\n203 KB\n-91%",
        "hero\nJPEG -> WebP\n78 КБ\n61 КБ\n~22%",
    ),
    (
        "hermes-rivera-aK6WGqxyHFw-unsplash\nJPEG -> WebP\n5.2 MB\n206 KB\n-96%",
        "gallery-1\nJPEG -> WebP\n93 КБ\n85 КБ\n~8%",
    ),
    (
        "johnny-africa-rRRyYQZpGmM-unsplash\nJPEG -> WebP\n5.4 MB\n261 KB\n-95%",
        "gallery-2\nJPEG -> WebP\n93 КБ\n90 КБ\n~3%",
    ),
    (
        "jonathan-skule-hvhpyxZtQMc-unsplash\nJPEG -> WebP\n4.9 MB\n190 KB\n-96%",
        "gallery-3\nJPEG -> WebP\n22 КБ\n13 КБ\n~40%",
    ),
    (
        "molly-bailey-y32fU_cRL44-unsplash\nJPEG -> WebP\n4.7 MB\n178 KB\n-95%",
        "gallery-3 (web.html)\nJPEG -> WebP\n22 КБ\n13 КБ\n~40%",
    ),
    (
        "organic-vineyard-chianti-region-ripe-grapes...\nJPEG -> WebP\n6.9 MB\n285 KB\n-96%",
        "(видалено — дубль hero)\n—\n—\n—\n—",
    ),
    (
        "Рис. 2.1. Процес стиснення зображення у формат WebP через інструмент Squoosh",
        "Рис. 2.1. Процес стиснення зображення у формат WebP через інструмент Squoosh\n\n"
        "▶ Скріншот: squoosh.app → завантажити assets/img/lab03/hero.jpg → WebP 82% → вставити порівняння розміру.",
    ),
    (
        '<img class="image add-top-margin-small add-bottom-margin" src="img/alexander-ugolkov-TkGI3Mkdurk-unsplash.jpg" alt="Келих червоного вина на столі під час дегустації">',
        '<img src="assets/img/lab03/hero.jpg" alt="Ілюстрація технічного SEO-аудиту" width="1200" height="600">',
    ),
    (
        '<source srcset="img/alexander-ugolkov-TkGI3Mkdurk-unsplash.webp" type="image/webp">\n<img class="image add-top-margin-small add-bottom-margin" \nsrc="img/alexander-ugolkov-TkGI3Mkdurk-unsplash.jpg" \nalt="Келих червоного вина на столі під час дегустації" \nwidth="600" \nheight="400">',
        '<source srcset="assets/img/lab03/hero.webp" type="image/webp">\n<img class="hero-image" src="assets/img/lab03/hero.jpg"\nalt="Ілюстрація технічного SEO-аудиту" width="1200" height="600">',
    ),
    (
        "Аналогічним чином я переписав код для інших фотографій товарів на сайті",
        "Аналогічно оновлено gallery-1..3 на index.html та зображення на services/web.html (див. репозиторій).",
    ),
    (
        "Рис. 2.2. Візуальне відображення сторінки до оптимізації",
        "Рис. 2.2. Сторінка до оптимізації (JPEG без WebP)\n\n▶ Скріншот: головна до git push Lab 03 або локально на старому коміті.",
    ),
    (
        "Рис. 2.3. Візуальне відображення сторінки після імплементації стиснених WebP зображень (якість не втрачено)",
        "Рис. 2.3. Сторінка після WebP + <picture>\n\n▶ Скріншот: https://justiksss.github.io/seo-lab-01-site/ після деплою.",
    ),
    (
        "Головний банер (organic-vineyard-chianti-region-ripe-grapes...) завантажується одразу без lazy loading.",
        "Hero (assets/img/lab03/hero.webp / hero.jpg) завантажується одразу без lazy loading.",
    ),
    (
        "А от всім іншим картинкам (картки товарів у галереї) я додав атрибут loading=\"lazy\".",
        "Галереї gallery-1..3 та зображенню на services/web.html додано loading=\"lazy\".",
    ),
    (
        "alexander-ugolkov-TkGI3Mkdurk-unsplash.jpg (Товар 1)\nhermes-rivera-aK6WGqxyHFw-unsplash.jpg (Товар 2)\njohnny-africa-rRRyYQZpGmM-unsplash.jpg (Товар 3)\njonathan-skule-hvhpyxZtQMc-unsplash.jpg (Товар 4)\nmolly-bailey-y32fU_cRL44-unsplash.jpg (Товар 5)",
        "gallery-1.jpg / .webp (index.html, галерея)\ngallery-2.jpg / .webp (index.html)\ngallery-3.jpg / .webp (index.html + services/web.html)",
    ),
    (
        "При оновленні сторінки (без прокрутки) завантажилося лише лого та головний банер. Тільки коли я почав скролити сторінку вниз, у списку Network почали з'являтися запити на завантаження решти картинок (Товар 1, Товар 2 і т.д.).",
        "Після hard reload (Cmd+Shift+R) без прокрутки завантажується hero; після скролу до галереї з'являються запити gallery-1..3.webp.",
    ),
    (
        "Рис. 3.1. Вкладка Network у DevTools, що підтверджує поступове (відкладене) завантаження зображень при скролінгу",
        "Рис. 3.1. Network (Img) — відкладене завантаження\n\n"
        "▶ Скріншот: F12 → Network → Img → reload без скролу; другий скрін — після скролу до галереї.",
    ),
    (
        "Я створив цей файл у редакторі коду та прописав базові правила для інтернет-магазину.",
        "Файл оновлено у корені репозиторію з правилами для навчального SEO-сайту (Lab 01–03).",
    ),
    (
        "User-agent: *\nDisallow: /empty.html\nDisallow: /embedding.html\nDisallow: /widgets.html\nAllow: /\n\nSitemap: https://makss-gil.github.io/learn-seo-hilitukha/sitemap.xml",
        "User-agent: *\nDisallow: /redirect-a.html\nDisallow: /redirect-b.html\nDisallow: /redirect-c.html\nDisallow: /duplicate-title-1.html\nDisallow: /duplicate-title-2.html\nAllow: /\n\nSitemap: https://justiksss.github.io/seo-lab-01-site/sitemap.xml",
    ),
    (
        "Disallow: /empty.html (та інші файли з цієї групи) — забороняє роботам сканувати технічні файли-заглушки, які залишилися від початкового шаблону і не несуть користі для SEO. Це зроблено для економії краулінгового бюджету (щоб Гугл витрачав час на товари, а не на сміття).",
        "Disallow для redirect-a/b/c та duplicate-title-1/2 — заборона обходу навчальних сторінок з ланцюгами редиректів і дубльованими title (Lab 01), щоб краулінговий бюджет витрачався на корисний контент.",
    ),
    (
        "Allow: / — дозволяє сканувати всі інші сторінки сайту (категорії, товари, блог).",
        "Allow: / — дозволяє індексувати головну, about, blog, services, faq тощо.",
    ),
    (
        "Для того, щоб пошукові роботи могли швидко та ефективно знаходити всі важливі сторінки мого інтернет-магазину, я створив карту сайту. Файл розміщено на моєму ресурсі за адресою: https://makss-gil.github.io/learn-seo-hilitukha/sitemap.xml.",
        "Для індексації навчальних сторінок створено sitemap.xml у корені сайту: https://justiksss.github.io/seo-lab-01-site/sitemap.xml.",
    ),
    (
        "Однак автоматичний генератор витягнув зайві сторінки (наприклад, faq.html) і пропустив частину важливих карток товарів. Тому я вручну відредагував код, залишивши рівно 10 цільових URL-адрес (головна, категорії, товари та блог).",
        "Файл відредаговано вручну: 8 пріоритетних URL (головна, about, contact, faq, glossary, services, blog) з тегами lastmod, changefreq, priority. Сторінки з Disallow у robots.txt у sitemap не включені.",
    ),
    (
        "https://makss-gil.github.io/learn-seo-hilitukha/sitemap.xml",
        "https://justiksss.github.io/seo-lab-01-site/sitemap.xml",
    ),
    (
        "Рис. 5.1. Відображення вмісту згенерованого та відредагованого файлу sitemap.xml у браузері.",
        "Рис. 5.1. sitemap.xml у браузері\n\n▶ Скріншот: відкрити URL sitemap.xml у браузері → вставити зображення.",
    ),
    (
        "Рис. 5.2. Підтвердження фізичної доступності файлу sitemap.xml для пошукового робота Google через інструмент тестування URL-адреси.",
        "Рис. 5.2. GSC — Sitemaps або URL Inspection\n\n"
        "▶ Скріншот: Search Console → Sitemaps → sitemap.xml (Submit/Success) або Test Live URL.",
    ),
    (
        "48 / 100",
        "[Mobile: заповнити]",
    ),
    (
        "72 / 100",
        "[Desktop: заповнити]",
    ),
    (
        "5.8 сек",
        "[заповнити]",
    ),
    (
        "2.4 сек",
        "[заповнити]",
    ),
    (
        "0.18",
        "[заповнити]",
    ),
    (
        "2.1 сек",
        "[заповнити]",
    ),
    (
        "Performance Score\n73\n78\n75\n98\nLCP (Largest Contentful Paint)\n105,5 с\n4,0 с\n16,9 с\n0,9 с",
        "Performance Score\n[M до]\n[M після]\n[D до]\n[D після]\nLCP\n[заповнити]\n[заповнити]\n[заповнити]\n[заповнити]",
    ),
    (
        "Рис. 6.1. Результати PageSpeed Insights для мобільної версії після оптимізації (78 балів).",
        "Рис. 6.1. PageSpeed Mobile після оптимізації\n\n▶ Скріншот: PageSpeed → Mobile після git push Lab 03.",
    ),
    (
        "Рис. 6.2. Результати PageSpeed Insights для десктопної версії після оптимізації (98 балів).",
        "Рис. 6.2. PageSpeed Desktop після оптимізації\n\n▶ Скріншот: PageSpeed → Desktop після оптимізації.",
    ),
    (
        "Аналіз досягнутих покращень: Найголовнішим досягненням стала колосальна оптимізація метрики LCP (час відображення найбільшого елемента). На мобільних пристроях цей показник знизився з критичних 105,5 секунд до 4,4 секунд, а на десктопі — з 16,9 с до 0,9 с (зелена зона). Це стало можливим виключно завдяки стисненню важкого фонового зображення через Squoosh (зменшення розміру на понад 90%) та конвертації його у формат WebP. Десктопна версія досягла майже еталонного показника у 98 балів, що свідчить про правильне налаштування lazy loading для зображень нижче першого екрана.",
        "Аналіз досягнутих покращень: після впровадження WebP, <picture>, width/height та lazy loading для галереї очікується зниження LCP і зменшення початкового обсягу завантаження. Точні значення вносяться в таблицю 6.1 після повторного тесту PageSpeed Insights для https://justiksss.github.io/seo-lab-01-site/.",
    ),
    (
        "Аналіз залишкових проблем та нереалізованих оптимізацій: Хоча десктопна версія працює ідеально, мобільна версія зупинилася на позначці 78 балів (жовта зона). Головна проблема, яку вказує PageSpeed Insights — це «Запити, що блокують відображення» (Render-blocking resources). Інструмент скаржиться на файли стилів (frame.css, controls.css, custom.css) та зовнішні бібліотеки (FontAwesome, Google Fonts).\nУ межах поточної лабораторної роботи повністю усунути цю проблему неможливо з технічних причин. Для того, щоб зняти блокування CSS, необхідно впровадити технологію Critical CSS (витягнути стилі першого екрана та вбудувати їх інлайново в HTML, а решту завантажувати асинхронно). Оскільки мій сайт використовує готовий статичний шаблон, спроба відкласти завантаження основних CSS-файлів призводить до ефекту FOUC (Flash of Unstyled Content) — сторінка на секунду відображається у вигляді \"голого\" тексту без дизайну, що критично погіршує досвід користувача. Також я застосував атрибут defer до скриптів (jquery.min.js), що частково зняло навантаження, але для досягнення 100 балів на мобільному потрібна повна перезбірка архітектури сайту з використанням сучасних бандлерів (наприклад, Webpack або Vite), що виходить за рамки поточного завдання з базового технічного SEO.",
        "Аналіз залишкових проблем: на навчальному сайті один файл assets/css/style.css є render-blocking — це типова ситуація для статичного HTML. Повне усунення потребує Critical CSS або бандлера (Vite/Webpack), що виходить за рамки Lab 03. Також Field Data в PageSpeed оновлюється із затримкою; для оцінки щойно зроблених змін використовуй Lab Data.",
    ),
    (
        "Під час виконання лабораторної роботи я здійснив комплексний технічний аудит та оптимізацію інтернет-магазину.",
        "Під час виконання лабораторної роботи здійснено технічний аудит та оптимізацію навчального сайту SEO Lab 01.",
    ),
    (
        "зменшити їхню вагу в середньому на 95%",
        "зменшити розмір файлів (hero до ~22%, gallery-3 до ~40% — див. табл. 2.1)",
    ),
    (
        "makss-gil.github.io/learn-seo-hilitukha",
        "justiksss.github.io/seo-lab-01-site",
    ),
    (
        "Nice Wine",
        "SEO Lab",
    ),
    (
        "інтернет-магазину",
        "навчального SEO-сайту",
    ),
    (
        "інтернет-магазин",
        "навчальний сайт SEO Lab",
    ),
]


def load_docs_service():
    data = json.loads(CREDS_PATH.read_text())
    creds = Credentials.from_authorized_user_info(data)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("docs", "v1", credentials=creds)


def apply_replacements(docs, doc_id: str) -> list[dict]:
    requests = []
    for old, new in REPLACEMENTS:
        if old == new:
            continue
        requests.append(
            {
                "replaceAllText": {
                    "containsText": {"text": old, "matchCase": True},
                    "replaceText": new,
                }
            }
        )
    # Google Docs API limit: batch in chunks
    results = []
    chunk_size = 40
    for i in range(0, len(requests), chunk_size):
        chunk = requests[i : i + chunk_size]
        resp = (
            docs.documents()
            .batchUpdate(documentId=doc_id, body={"requests": chunk})
            .execute()
        )
        results.append(resp)
    return results


def main() -> int:
    docs = load_docs_service()
    print(f"Updating document {DOC_ID}...")
    responses = apply_replacements(docs, DOC_ID)
    print(f"Done. batches={len(responses)}")
    creds = Credentials.from_authorized_user_info(json.loads(CREDS_PATH.read_text()))
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    drive = build("drive", "v3", credentials=creds)
    drive.files().update(
        fileId=DOC_ID,
        body={"name": "lab3-seo-justiksss"},
    ).execute()
    print("Renamed to: lab3-seo-justiksss")
    return 0


if __name__ == "__main__":
    sys.exit(main())
