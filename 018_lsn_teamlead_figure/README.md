# 🧠 Проєкт: ООП Наслідування + Абстрактні Класи (TeamLead + Фігури)

Цей проєкт охоплює два ключові напрямки об'єктно-орієнтованого програмування в Python:

1. **Множинне та ромбовидне наслідування** (класи `Employee`, `Manager`, `Developer`, `TeamLead`)
2. **Абстрактні класи та реалізація геометричних фігур** (`Figure`, `Rectangle`, `Circle`, `Triangle`)

---

## 📦 Структура проєкту

```
oop_inheritance_project/
├── team_lead_class.py         # Реалізація класів Employee, Manager, Developer, TeamLead
├── team_lead_example.py       # Приклад використання класу TeamLead
├── figure_class.py            # Абстрактний клас Figure та реалізація Rectangle, Circle, Triangle
├── figure_example.py          # Демонстрація розрахунків площі і периметру фігур
├── test_teamlead_props.py     # Pytest: тестування атрибутів класу TeamLead
├── test_figures.py            # Pytest: тестування геометричних фігур
├── requirements.txt           # Залежності проєкту
└── README.md                  # Документація (цей файл)
```

---

## 👨‍💼 Множинне наслідування: TeamLead

- `Employee`: базовий клас з `name` та `salary`
- `Manager`: успадковується від Employee, додає `department`
- `Developer`: успадковується від Employee, додає `programming_language`
- `TeamLead`: наслідує **обидва** класи (ромбовидне наслідування), додає `team_size`

📌 У класі `TeamLead` виклик `Employee.__init__()` виконується **напряму**.  
Атрибути `department` і `programming_language` додаються **вручну**, без `super()`.

✅ Тести перевіряють:

- наявність усіх потрібних атрибутів;
- правильність ініціалізації;
- форматований вивід (__str__).

---

## 📐 Абстрактні фігури: Rectangle, Circle, Triangle

Використано абстрактний клас `Figure` з методами `area()` та `perimeter()`.  
Наслідування реалізовано для:

- `Rectangle`: площа = width * height, периметр = 2(width + height)
- `Circle`: площа = π * r², периметр = 2πr
- `Triangle`: формула Герона для площі

📌 Конструктори перевіряють коректність даних.  
📌 Всі параметри (`__radius`, `__side_a`, `__width`, ...) — **приватні**.

✅ Тести перевіряють:

- обчислення площі та периметру;
- обробку некоректних даних;
- edge cases: негативні значення, неможливий трикутник.

---

## 🔧 Як запустити

1. Створи віртуальне середовище та активуй його:

```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
source .venv/bin/activate    # macOS/Linux
```

2. Встанови залежності:

```bash
pip install -r requirements.txt
```

3. Запусти приклади:

```bash
python team_lead_example.py
python figure_example.py
```

---

## 🧪 Запуск тестів

```bash
pytest
```

📋 Покривається:

- TeamLead: атрибути name, salary, department, language, team_size
- Фігури: значення площі/периметру, помилки ініціалізації

---

## 🧠 Автор

Проєкт створено в рамках навчального курсу з Python.  
**Den Kovylin**, майстер тасок, рефакторингу і README 😎
