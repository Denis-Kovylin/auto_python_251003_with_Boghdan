import sqlite3

conn = sqlite3.connect("hogwarts.db")
cursor = conn.cursor()

cursor.execute("SELECT id, first_name, last_name, email FROM students ORDER BY id")
rows = cursor.fetchall()

print("🧙‍♂️ Students in database:")
for row in rows:
    print(f"  ID: {row[0]} | Name: {row[1]} {row[2]} | Email: {row[3]}")

conn.close()
