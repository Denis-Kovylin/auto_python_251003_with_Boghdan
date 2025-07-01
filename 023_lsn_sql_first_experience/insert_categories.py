import sqlite3

categories = [
    ("Pistols",),
    ("Submachine Guns",),
    ("Assault Rifles",),
    ("Machine Guns",),
    ("Sniper Rifles",)
]

conn = sqlite3.connect("gunstore.db")
cursor = conn.cursor()

cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

conn.commit()
conn.close()

print("✅ Categories inserted successfully.")
