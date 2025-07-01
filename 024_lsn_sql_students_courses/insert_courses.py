import sqlite3

courses = [
    ("Potions",),
    ("Defense Against the Dark Arts",),
    ("Transfiguration",),
    ("Herbology",),
    ("Charms",)
]

conn = sqlite3.connect("hogwarts.db")
cursor = conn.cursor()

cursor.executemany("INSERT INTO courses (name) VALUES (?)", courses)

conn.commit()
conn.close()

print("✅ Courses inserted successfully.")
