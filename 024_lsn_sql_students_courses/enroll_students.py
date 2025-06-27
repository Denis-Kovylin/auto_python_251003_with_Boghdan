import sqlite3
import random

# Подключение к БД
conn = sqlite3.connect("hogwarts.db")
cursor = conn.cursor()

# Получаем список всех student_id и course_id
cursor.execute("SELECT id FROM students")
student_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM courses")
course_ids = [row[0] for row in cursor.fetchall()]

# Распределяем студентов по курсам случайным образом
enrollments = []
for student_id in student_ids:
    # Каждый студент будет записан минимум на 1 курс, максимум на 3
    enrolled_courses = random.sample(course_ids, k=random.randint(1, 3))
    for course_id in enrolled_courses:
        enrollments.append((student_id, course_id))

# Добавляем записи в таблицу enrollments
cursor.executemany("""
    INSERT OR IGNORE INTO enrollments (student_id, course_id)
    VALUES (?, ?)
""", enrollments)

conn.commit()
conn.close()

print("✅ Students enrolled in courses successfully.")
