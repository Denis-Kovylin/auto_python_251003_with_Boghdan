import sqlite3

conn = sqlite3.connect("hogwarts.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT 
        students.id,
        students.first_name || ' ' || students.last_name AS full_name,
        courses.name AS course_name
    FROM enrollments
    JOIN students ON enrollments.student_id = students.id
    JOIN courses ON enrollments.course_id = courses.id
    ORDER BY students.id, course_name
""")

rows = cursor.fetchall()

print("📝 Enrollments:")
for row in rows:
    print(f"  Student ID: {row[0]} | Name: {row[1]} | Course: {row[2]}")

conn.close()
