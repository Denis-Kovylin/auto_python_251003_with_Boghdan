# ❤️ Heartbeat Log Analyzer

Проект для автоматизированного анализа логов heartbeat, в которых мониторинг-система клиента должна отсылать сигнал
работоспособности каждые 30–31 секунду.  
Анализируется интервал между событиями и, если он превышает допустимые границы, логируется `WARNING` или `ERROR`.

---

## 📁 Структура проекта

```
022_lsn_time_heartbeat/
├── checker/
│   ├── heartbeat_analyzer.py    # Основная логика анализа
│   └── logger.py                # Конфигурация логгера
├── logs/
│   └── hb_test.log              # Результаты анализа
├── tests/
│   └── test_heartbeat.py        # Тест для Pytest
├── hblog.txt                    # Входной лог-файл
├── main.py                      # Точка входа
├── requirements.txt             # Зависимости
└── README.md                    # Документация проекта
```

---

## 🧠 Логика

- Если интервал между событиями **> 31 и < 33 сек** → `⚠️ WARNING`
- Если интервал **≥ 33 сек** → `❌ ERROR`
- Всё логируется в `logs/hb_test.log` и выводится в консоль
- Парсинг времени: `Timestamp 05:45:09` → `datetime.strptime("%H:%M:%S")`

---

## 🔧 Установка и запуск

1. Клонировать проект:

```bash
git clone https://github.com/yourname/heartbeat-analyzer.git
cd heartbeat-analyzer
```

2. Создать виртуальное окружение:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/macOS
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Запустить анализ:

```bash
python main.py
```

---

## ✅ Тесты

```bash
pytest
```

Проверяется:

- Анализ строки с интервалом > 31 сек
- Логирование `WARNING` и `ERROR`
- Правильность парсинга и записи

---

## 📌 Пример логов

```
2025-06-09 16:25:26,211 - ERROR - ❌ Превышен heartbeat: 35.0 сек — строка: { Trade Timestamp 04:50:42 Key TSTFEED0300|7E3E|0400 }
```

---

## 🧑‍💻 Автор

**Den Kovylin** — человек, у которого даже скрипты дышат по графику.
> "Каждому коду — свой ритм. А этот — пульс системы."
