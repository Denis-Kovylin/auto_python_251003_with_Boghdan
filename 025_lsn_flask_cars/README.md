# 🚗 Flask Cars API Testing

Цель проекта — протестировать Flask-приложение с аутентификацией и эндпоинтом `/cars`, используя Pytest, параметризацию
и логирование в файл.

## 🔧 Стек

- Flask
- flask_jwt_extended
- requests
- pytest

## 🚀 Как запустить сервер

1. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Запусти сервер:
   ```bash
   python cars_app.py
   ```

   Сервер будет доступен по адресу: [http://127.0.0.1:8080](http://127.0.0.1:8080)

## 🔐 Аутентификация

POST `/auth`  
Basic Auth:

- Username: `test_user`
- Password: `test_pass`

Ответ:

```json
{
  "access_token": "<токен>"
}
```

## 🚘 Эндпоинт `/cars`

Метод: `GET`  
Параметры запроса:

- `sort_by` — поле сортировки (например, `price`, `year`)
- `limit` — ограничение количества результатов

Заголовки:

```
Authorization: Bearer <токен>
```

## 🧪 Тестирование

1. Запусти сервер (если ещё не запущен).
2. Запусти тесты:
   ```bash
   pytest test_search_cars.py
   ```

3. Все запросы логируются в файл `test_search.log`.

## 📁 Структура проекта

```
├── cars_app.py             # Flask-сервер
├── test_search_cars.py     # Pytest с параметризацией
├── conftest.py             # Фикстура для сессии и логгера
├── logger_config.py        # Логгер
├── test_search.log         # Логи запросов
├── requirements.txt
└── README.md
```

## ✅ Реализация требований

- ✅ Flask сервер с токенами и эндпоинтом `/cars`
- ✅ Аутентификация через фикстуру (scope='class')
- ✅ Запросы с использованием `requests.Session`
- ✅ Pytest с параметризацией (7 наборов данных)
- ✅ Логирование в консоль и `test_search.log`

## 🧠 Автор

Skynet & Human — слаженная команда, уничтожающая API-баги, пока ты спишь 😎
