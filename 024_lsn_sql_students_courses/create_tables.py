import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("hogwarts.db")
cursor = conn.cursor()

# Загрузка и выполнение SQL-скрипта
with open("init_schema.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

cursor.executescript(sql_script)

conn.commit()
conn.close()

print("✅ Tables created successfully.")
