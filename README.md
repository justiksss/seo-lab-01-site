# SEO Lab 01 — тестовий сайт

Навчальний статичний сайт для лабораторної «Аудит сайту».

## Навмисні проблеми для аудиту

| Тип | Де шукати |
|-----|-----------|
| 404 | `broken-link-target.html`, `old-article-removed.html` (посилання з index, faq) |
| Без title | `page-no-title.html` |
| Дублікат контенту | `blog/post-duplicate-a.html` ↔ `post-duplicate-b.html` |
| Дубль title | `duplicate-title-1.html`, `duplicate-title-2.html` |
| Ланцюг редиректів | `redirect-a.html` → b → c → `redirect-final.html` |
| Зображення без alt | `services/web.html` |

## Публікація на GitHub Pages

1. Створіть репозиторій `seo-lab-01-site` на GitHub.
2. Замініть `USERNAME` у `sitemap.xml`, `robots.txt`, `index.html` (canonical) на ваш логін GitHub.
3. Завантажте файли (`git push`).
4. **Settings → Pages → Source:** Deploy from branch `main`, folder `/ (root)`.
5. Сайт: `https://ВАШ_ЛОГІН.github.io/seo-lab-01-site/`

## Локальний перегляд

```bash
cd /Users/justiksss/Projects/seo-lab-01-site
python3 -m http.server 8080
```

Відкрийте http://localhost:8080
