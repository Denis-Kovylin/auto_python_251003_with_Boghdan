from stdnt_class import Student


# 🔹 Створюємо екземпляр класу
student_x = Student("Denis", "Kovylin", 27, 88)

# 🔹 Друкуємо початкову інформацію
print("До зміни балу:")
print(student_x)

# 🔹 Використовуємо зміни балу метод
student_x.set_average_grade(75)

# 🔹 Друкуємо оновлену інформацію
print("\nПісля зміни балу:")
print(student_x)