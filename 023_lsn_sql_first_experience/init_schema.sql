--Создание таблицы категорий
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

--Создание таблицы продуктов
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    weight REAL,
    price REAL,
    length TEXT,
    caliber TEXT,
    effective_range TEXT,
    country_of_origin TEXT NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

