# Task Manager API

REST API для управления задачами, разработанный на **FastAPI** с использованием современной архитектуры backend-приложений.

## Возможности

### Задачи

* Создание задачи
* Получение списка задач
* Получение задачи по ID
* Обновление задачи
* Удаление задачи
* Пагинация
* Поиск
* Фильтрация
* Сортировка

### Пользователи

* Регистрация
* Авторизация
* JWT-аутентификация
* Хеширование паролей (bcrypt)

### Безопасность

* JWT Access Token
* Защита маршрутов
* Пользователь имеет доступ только к своим задачам

### Инфраструктура

* PostgreSQL
* SQLAlchemy 2.x (Async)
* Alembic
* Docker
* Docker Compose
* Логирование
* Обработка пользовательских исключений

---

# Стек технологий

* Python 3.10+
* FastAPI
* SQLAlchemy 2.x
* AsyncPG
* Alembic
* PostgreSQL
* Pydantic v2
* JWT (PyJWT)
* Passlib + bcrypt
* Docker
* Docker Compose
* Pytest
* Ruff
* Black

---


# Архитектура приложения

Проект реализован по многослойной архитектуре.

```
Client

↓

Router

↓

Service

↓

Repository

↓

Database
```

### Router

Отвечает за HTTP-запросы и ответы.

### Service

Содержит бизнес-логику приложения.

### Repository

Работает исключительно с базой данных.

### Database

PostgreSQL.

---

# Запуск проекта

## Клонирование

```bash
git clone https://github.com/<username>/<repository>.git
```

```bash
cd pet_base
```

---

## Создание .env

Пример:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/pet_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Запуск через Docker

```bash
docker compose up --build
```

После запуска будут автоматически выполнены:

* запуск PostgreSQL
* применение миграций Alembic
* запуск FastAPI

---

## Документация API

Swagger:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

# Авторизация

Получение JWT:

```
POST /auth/login
```

После получения токена необходимо нажать кнопку **Authorize** в Swagger и вставить:

```
Bearer <JWT_TOKEN>
```

После этого будут доступны защищенные маршруты.

---

# Миграции

Создание миграции:

```bash
alembic revision --autogenerate -m "message"
```

Применение:

```bash
alembic upgrade head
```

Откат:

```bash
alembic downgrade -1
```

---

# Тестирование

Запуск тестов:

```bash
pytest
```

Покрытие:

```bash
pytest --cov
```

---

# Возможности проекта

* Регистрация пользователей
* JWT-аутентификация
* CRUD задач
* Фильтрация
* Поиск
* Сортировка
* Пагинация
* Пользователь имеет доступ только к собственным задачам
* Логирование
* Обработка исключений
* Docker
* Alembic

---

# Планы развития

* Refresh Token
* Redis
* Celery
* Отправка Email
* Загрузка файлов
* GitHub Actions (CI/CD)
* Nginx
* Gunicorn
* Мониторинг приложения
* Интеграционные тесты
* Health Check

---

# Автор

Проект разработан в качестве pet-проекта для изучения современных технологий Python Backend-разработки и демонстрации практических навыков работы с FastAPI, SQLAlchemy, PostgreSQL и Docker.
