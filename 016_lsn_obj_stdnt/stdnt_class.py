class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__average_grade = average_grade

    def get_average_grade(self):
        return self.__average_grade

    def set_average_grade(self, value: int):
        if isinstance(value, int) and value > 0:
            self.__average_grade = value
        else:
            raise ValueError("Невірний формат середнього балу!")

    def __str__(self):
        return (
            f"Студент: {self.first_name} {self.last_name}\n"
            f"Вік: {self.age}\n"
            f"Середній бал: {self.get_average_grade()}"
        )

