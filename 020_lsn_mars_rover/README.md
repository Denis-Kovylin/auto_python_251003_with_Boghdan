# 🚀 Mars Rover Photo Downloader

Проект для скачивания фотографий, сделанных марсоходом **Curiosity**, с использованием открытого API NASA.  
Извлекает ссылки на фото по заданным параметрам, скачивает их и сохраняет в локальную папку `images/`.

## 📦 Структура проекта

```
020_lsn_mars_rover/
├── images/                   # Папка для скачанных фото
├── main.py                   # Точка входа: запуск скачивания
├── mars_client/
│   └── api_client.py         # Класс клиента для общения с NASA API
├── tests/
│   └── test_nasa_api_client.py  # Тесты на Pytest
├── requirements.txt          # Все зависимости проекта
└── README.md                 # Документация проекта (ты сейчас здесь)
```

## 🧠 Используемый стек

- Python 3.12+
- requests
- pytest

## 🔧 Установка и запуск

1. Клонируй репозиторий:

```bash
git clone https://github.com/yourname/mars-rover-photo-downloader.git
cd mars-rover-photo-downloader
```

2. Создай виртуальное окружение и активируй:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac
```

3. Установи зависимости:

```bash
pip install -r requirements.txt
```

4. Запусти основной скрипт:

```bash
python main.py
```

В консоли появится статус загрузки и файлы сохранятся в папку `images/`.

## ✅ Тесты

Запусти тесты с помощью Pytest:

```bash
pytest
```

Тесты проверяют:

- возвращаемый формат (`list`)
- структуру объектов (наличие ключа `img_src` и корректность URL)

## 📸 Пример вывода

```
Фотокартку 1 збережено: mars_photo1.jpg
Фотокартку 2 збережено: mars_photo2.jpg
```

## ✨ Примечание

В качестве ключа API используется `DEMO_KEY`. Его хватает для 30 запросов в час.  
Для частого использования рекомендуем получить [свой API ключ на сайте NASA](https://api.nasa.gov).

## 🧠 Автор

Проект выполнен в рамках курса по автоматизации.  
Автор: **Den**, aka человек, который пробился через боль, слёзы и PyCharm ради пары фоток с Марса.

---

> “Curiosity is the essence of human existence.”  
> — Gene Cernan, астронавт, последний человек на Луне
