# 🖼️ Flask Image API Client

Проект демонстрирует работу клиент-серверного взаимодействия с использованием **Flask** и **requests**.  
Сервер принимает изображение, сохраняет его в папку `uploads/`, позволяет получить его URL или байты, а также удалить.

Клиентская часть реализована в виде класса `ImageApiClient`, который выполняет следующие действия:

- загружает изображение на сервер (`POST /upload`);
- получает URL изображения в формате JSON (`GET /image/<filename>`);
- получает изображение как байты (`GET /image/<filename>` с заголовком);
- удаляет изображение (`DELETE /delete/<filename>`).

---

## 📁 Структура проекта

```
021_lsn_flask_image/
├── app/
│   ├── app.py                # Flask сервер
│   └── __init__.py
├── client/
│   ├── image_client.py       # Класс ImageApiClient
│   ├── main.py               # Скрипт для демонстрации работы клиента
│   └── __init__.py
├── tests/
│   ├── test_image_client.py  # Pytest-тесты для клиента
│   └── __init__.py
├── images/                   # Папка с test_image.jpg и downloaded.jpg
├── uploads/                  # Папка, куда сервер сохраняет загруженные изображения
├── requirements.txt          # Зависимости проекта
└── README.md                 # Ты сейчас здесь 😎
```

---

## 🧠 Используемый стек

- Python 3.12+
- Flask
- requests
- pytest

---

## ▶️ Как запустить

### 1. Клонируй проект и перейди в папку:

```bash
git clone https://github.com/yourname/flask-image-api-client.git
cd flask-image-api-client
```

### 2. Создай и активируй виртуальное окружение:

```bash
python -m venv flask_venv
flask_venv\Scripts\activate        # Windows
source flask_venv/bin/activate     # Mac/Linux
```

### 3. Установи зависимости:

```bash
pip install -r requirements.txt
```

---

## 🚀 Как пользоваться

### 1. Запусти сервер:

```bash
python app/app.py
```

Сервер стартует на `http://127.0.0.1:8080`.

### 2. Запусти клиент (в другом окне терминала):

```bash
python client/main.py
```

Будет загружено изображение `images/test_image.jpg`, сохранено на сервере, затем загружено обратно как
`images/downloaded.jpg`.

---

## ✅ Запуск тестов

```bash
pytest
```

Проверяются:

- загрузка изображения (`POST /upload`)
- получение URL изображения (`GET /image/<filename>`)
- получение байтов изображения
- удаление изображения (`DELETE /delete/<filename>`)

---

## 📝 Примечания

- Перед запуском убедись, что папки `uploads/` и `images/` существуют.
- Если удалишь `uploads/` — создай её заново, иначе `POST /upload` даст 500 ошибку.
- Все пути указываются **относительно исполняемых файлов**.

---

## 👨‍💻 Автор

**Den K.** — чувак, который заставил эту хрень заработать, даже когда PyCharm ломал его дух.  
Этот README — результат боли, страданий, 500-х ошибок и победы над путями.

---
> 🧠 "API без тестов — как пончик без начинки. Формально работает, но радости мало."
