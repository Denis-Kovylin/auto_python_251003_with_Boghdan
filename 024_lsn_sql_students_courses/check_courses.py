import sqlite3

conn = sqlite3.connect("hogwarts.db")
cursor = conn.cursor()

cursor.execute("SELECT id, name, description FROM courses ORDER BY id")
rows = cursor.fetchall()

print("📚 Courses in database:")
for row in rows:
    print(f"  ID: {row[0]} | Name: {row[1]} | Description: {row[2]}")

conn.close()
