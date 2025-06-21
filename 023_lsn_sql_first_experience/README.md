# Gunstore Database Project

This project creates and manages a structured SQLite database for a fictional firearms online store. It includes two
main entities:

* `categories`: for weapon types (e.g., Pistols, Sniper Rifles).
* `products`: for detailed data on legendary firearms from the USA, USSR, Germany, etc.

---

## 📦 Project Structure

```
firearm_gunstore_project/
├── gunstore.db               # SQLite database file
├── init_schema.sql          # SQL schema with table definitions
├── create_tables.py         # Script to create tables from schema
├── insert_categories.py     # Script to add weapon categories
├── insert_products.py       # Scripts to add products (batched per category)
├── check_categories.py      # View categories in the database
├── check_products.py        # View products with JOIN info
├── queries.sql              # Collection of sample SQL queries (JOINs, filters)
├── requirements.txt         # pip dependencies (sqlite3 built-in)
└── README.md                # You are here
```

---

## 🔧 Setup & Usage

1. **Clone the project or copy files into a directory.**

2. **Create and populate the database:**

```bash
python create_tables.py
python insert_categories.py
python insert_products.py
```

3. **Check data (optional):**

```bash
python check_categories.py
python check_products.py
```

4. **Explore data via SQL queries:**

Use any SQLite GUI (e.g., Database Navigator in PyCharm or SQLite Viewer plugin). Load `gunstore.db` and run queries
from `queries.sql`.

---

## 🧠 Example Queries

```sql
-- Get all pistols
SELECT name, price FROM products WHERE category_id = 1;

-- Show product names and their category
SELECT p.name, p.country_of_origin, c.name as category
FROM products p
JOIN categories c ON p.category_id = c.id;

-- Sniper rifles with price over $8000
SELECT name, price FROM products WHERE category_id = 5 AND price > 8000;

-- All weapons made in Germany
SELECT name, description FROM products WHERE country_of_origin = 'Germany';
```

---

## 🛠 Technologies Used

* SQLite (no server needed)
* Python 3.12
* SQL (DDL, DML, JOIN)

---

## ✨ Inspiration

The dataset includes iconic weapons such as:

* 🇺🇸 Colt M1911, M16A2, Barrett M82
* 🇷🇺 AK-47, PKM, Dragunov SVD
* 🇩🇪 MP40, StG 44, MG42

This makes the project not only technically rich but also historically and culturally engaging.

---

## ✅ Author

Den — a guy who doesn’t want to sell bananas online, but legendary firearms in style.

> "God created men. Sam Colt made them equal."
