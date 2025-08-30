API-сервис для управления вопросами и ответами.  
Проект реализован на **Django Rest Framework** с использованием **PostgreSQL** в качестве базы данных и запускается
через **Docker Compose**.

## 🚀 Функционал

- Управление вопросами:
  - `GET /questions/` — список всех вопросов
  - `POST /questions/` — создать новый вопрос
  - `GET /questions/{id}` — получить вопрос и все ответы на него
  - `DELETE /questions/{id}` — удалить вопрос (вместе с ответами)

- Управление ответами:
  - `POST /questions/{id}/answers/` — добавить ответ к вопросу
  - `GET /answers/{id}` — получить конкретный ответ
  - `DELETE /answers/{id}` — удалить ответ

### 🔍 Бизнес-логика:
- Нельзя создать ответ к несуществующему вопросу.
- Один пользователь может оставлять несколько ответов к одному вопросу.
- Удаление вопроса приводит к каскадному удалению всех его ответов.

---

## 🛠️ Стек технологий
- Python 3.11+
- Django 5.x
- Django Rest Framework 3.x
- PostgreSQL 13+
- Docker, Docker Compose
- Django migrations

## 📦 Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/zednb/ask_api.git
cd ask_api

2. Настройка переменных окружения

Создайте файл .env в корне проекта и добавьте:

POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True

3. Запуск через Docker Compose
docker-compose up --build

После сборки проект будет доступен по адресу:
http://127.0.0.1:8000/

🔄 Миграции
После первого запуска выполните:
docker-compose exec web python manage.py migrate

🧪 Тестирование
Запуск тестов:
docker compose exec app pytest -v