# 🧠 Итератори, Генератори та Декоратори в Python

## 📚 Опис проєкту

Цей репозиторій містить приклади реалізації трьох ключових концепцій Python:

- 🔁 **Ітератори** — класи з методами `__iter__` і `__next__`.
- 🔄 **Генератори** — функції з `yield` для створення послідовностей.
- 🧙‍♂️ **Декоратори** — обгортки для додаткової логіки навколо функцій.

🛠 Для підтримки структури додано модуль `utils`, що містить:
- логгер;
- тестові дані: списки чисел, функції, тригер помилки.

---

## 📁 Структура проєкту

```
.
├── iterators/
│   ├── even_iterator.py
│   └── reverse_iterator.py
├── generators/
│   ├── even_generator.py
│   └── fibonacci_generator.py
├── decorators/
│   ├── exception_handler_decorator.py
│   └── logging_decorator.py
├── utils/
│   ├── logger.py
│   └── test_data.py
├── main.py
└── README.md
```

---

## ▶️ Як використовувати

Кожен файл (`*.py`) в папках `iterators/`, `generators/`, `decorators/` — це окрема демонстрація задачі.  
Їх можна запускати автономно:

```bash
python iterators/even_iterator.py
python generators/fibonacci_generator.py
python decorators/logging_decorator.py
```

Або запустити **всі приклади одразу через головний файл**:

```bash
python main.py
```

> ⚠️ Перед запуском переконайтесь, що активовано віртуальне середовище, та встановлено всі залежності (якщо є).

---

## 🔥 Автор

Den Ko aka "чувак, який довів README до ідеалу" 😎 ( Ахахахха, это конечно же сгенерировано при помоши ИИ, но все равно же круто? )
