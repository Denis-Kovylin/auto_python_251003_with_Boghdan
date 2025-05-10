class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__average_grade = average_grade

    def get_average_grade(self):
        return self.__average_grade

    def __str__(self):
        return (
            f"Студент: {self.first_name} {self.last_name}\n"
            f"Вік: {self.age}\n"
            f"Середній бал: {self.get_average_grade()}"
        )


# 🔹 Створюємо екземпляр класу
student_x = Student("Denis", "Kovylin", 27, 88)

# 🔹 Друкуємо початкову інформацію
print("До зміни балу:")
print(student_x)

# 🔹 Додаємо метод до класу після створення об'єкта
def set_average_grade(self, value: int):
    if isinstance(value, int) and value > 0:
        self._Student__average_grade = value  # доступ до приватного атрибута
    else:
        raise ValueError("Невірний формат середнього балу!")

Student.set_average_grade = set_average_grade

# 🔹 Використовуємо новий метод
student_x.set_average_grade(75)

# 🔹 Друкуємо оновлену інформацію
print("\nПісля зміни балу:")
print(student_x)
