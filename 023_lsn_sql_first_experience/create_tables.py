import sqlite3

# Подключаемся к базе данных (если нет — будет создана)
conn = sqlite3.connect("gunstore.db")
cursor = conn.cursor()

# Загружаем SQL-скрипт из файла
with open("init_schema.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

# Выполняем скрипт
cursor.executescript(sql_script)

print("✅ Tables created successfully.")
conn.commit()
conn.close()
