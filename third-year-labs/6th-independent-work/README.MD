### Поточна структура проекту Django:

```
blogger_info/
├── blogger_info/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── info_platform/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── index.html
│       ├── profile_list.html
│       └── profile_detail.html
├── manage.py
└── db.sqlite3
```

### Опис файлів та директорій:

- `blogger_info/`: Головна директорія проекту Django.

  - `__init__.py`: Ініціалізаційний файл пакету.
  - `asgi.py`: Конфігурація ASGI для асинхронного інтерфейсу сервера.
  - `settings.py`: Налаштування проекту.
  - `urls.py`: Головний файл маршрутизації проекту.
  - `wsgi.py`: Конфігурація WSGI для розгортання проекту.

- `info_platform/`: Додаток для інформаційної платформи.

  - `__init__.py`: Ініціалізаційний файл пакету.
  - `admin.py`: Налаштування адміністративної панелі.
  - `apps.py`: Конфігурація додатку.
  - `migrations/`: Директорія для файлів міграцій бази даних.
    - `__init__.py`: Ініціалізаційний файл пакету.
  - `models.py`: Моделі бази даних.
  - `tests.py`: Тести для додатку.
  - `urls.py`: Файл маршрутизації додатку.
  - `views.py`: Відображення для додатку.
  - `templates/`: Директорія для шаблонів HTML.
    - `index.html`: Шаблон для головної сторінки.
    - `profile_list.html`: Шаблон для сторінки списку профілів.
    - `profile_detail.html`: Шаблон для сторінки деталей профілю.

- `manage.py`: Скрипт для керування проектом Django.
- `db.sqlite3`: Файл бази даних SQLite.
