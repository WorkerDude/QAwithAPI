# QA Service API

API сервис для вопросов и ответов на базе FastAPI и PostgreSQL.

## Стек технологий

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Alembic (Миграции)
- Docker & Docker Compose
- Pytest

## Функционал

- Создание, чтение и удаление вопросов.
- Создание, чтение и удаление ответов.
- Каскадное удаление ответов при удалении вопроса.
- Валидация данных.

## Инструкция по запуску

### Предварительные требования
Убедитесь, что у вас установлены **Docker** и **Docker Compose**.

### Запуск

1. Клонируйте репозиторий:
   ```bash
   git clone <repository_url>
   cd qa_service