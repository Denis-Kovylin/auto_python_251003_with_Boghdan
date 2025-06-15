class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self,
                 name: str,
                 salary: float,
                 department: str,
                 programming_language: str,
                 team_size: int):
        # Явно вызываем базовый класс
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

    def __str__(self):
        return (
            f"Name: {self.name}, Salary: {self.salary}, "
            f"Dept: {self.department}, Lang: {self.programming_language}, "
            f"Team Size: {self.team_size}"
        )
