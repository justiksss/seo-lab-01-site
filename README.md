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
2. Завантажте файли (`git push`).
4. **Settings → Pages → Source:** Deploy from branch `main`, folder `/ (root)`.
5. Сайт: `https://ВАШ_ЛОГІН.github.io/seo-lab-01-site/`

## Lab 03 — технічна оптимізація

- Звіт (Markdown): `docs/lab-03-report.md`
- Скріншоти для PDF: `docs/lab-03-screenshots.md`
- Таблиця зображень: `docs/lab-03-image-inventory.md`

## Локальний перегляд

```bash
cd /Users/justiksss/Projects/seo-lab-01-site
python3 -m http.server 8080
```

Відкрийте http://localhost:8080
