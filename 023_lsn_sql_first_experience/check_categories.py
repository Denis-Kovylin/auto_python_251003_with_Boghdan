import sqlite3

conn = sqlite3.connect("gunstore.db")
cursor = conn.cursor()

cursor.execute("SELECT id, name FROM categories")
rows = cursor.fetchall()

print("📦 Categories in database:")
for row in rows:
    print(f"  ID: {row[0]} | Name: {row[1]}")

conn.close()
