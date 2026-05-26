# Lab 03 — інвентаризація зображень

| Файл | URL на сайті | Формат до | Розмір до | Формат після | Розмір після | Зменшення |
|------|--------------|-----------|-----------|--------------|--------------|-----------|
| hero | `/assets/img/lab03/hero.*` | JPEG | 78 КБ | WebP | 61 КБ | ~22% |
| gallery-1 | `/assets/img/lab03/gallery-1.*` | JPEG | 93 КБ | WebP | 85 КБ | ~8% |
| gallery-2 | `/assets/img/lab03/gallery-2.*` | JPEG | 93 КБ | WebP | 90 КБ | ~3% |
| gallery-3 | `/assets/img/lab03/gallery-3.*` | JPEG | 22 КБ | WebP | 13 КБ | ~40% |

> Для звіту додай скрін із **Squoosh** (якість 80–85%) — у таблиці звіту можна вказати розміри після повторного стиснення в Squoosh, якщо вони менші за `cwebp` у репозиторії.

**Атрибути в HTML:** усі `<img>` мають `alt`, `width`, `height`. Hero — без `loading="lazy"`; gallery та `services/web.html` — з `loading="lazy"`.
