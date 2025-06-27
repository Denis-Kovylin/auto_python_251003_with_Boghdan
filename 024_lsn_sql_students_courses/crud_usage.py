from hogwarts_crud import HogwartsCRUD

db = HogwartsCRUD()

# 1. Добавить нового студента и сразу записать на курс (например, курс с ID 2 — "Defense Against the Dark Arts")
db.add_student("Tom", "Riddle", "riddle.tom@hogwarts.edu", 2)

# 2. Обновить информацию о студенте
# (предположим, у него ID 21, можно уточнить ID в базе, если что)
db.update_student(21, email="lord.voldemort@hogwarts.edu")

# 3. Получить курсы, на которые записан студент
db.get_student_courses(21)

# 4. Получить студентов, записанных на определённый курс
db.get_course_students(2)

# 5. Удалить студента
db.delete_student(21)

# Завершить соединение с базой данных
db.close()
