class Employee:
    def __init__(self, name: str, salary: float, **kwargs):
        self.name = name
        self.salary = salary
        # не вызываем super — это самый «нижний» уровень


class Manager(Employee):
    def __init__(self, department: str, **kwargs):
        super().__init__(**kwargs)         # передаём name, salary и всё прочее
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language: str, **kwargs):
        super().__init__(**kwargs)         # передаём name, salary и всё прочее
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self,
                 name: str,
                 salary: float,
                 department: str,
                 programming_language: str,
                 team_size: int):
        super().__init__(
            department=department,
            programming_language=programming_language,
            name=name,
            salary=salary
        )
        self.team_size = team_size

    def __str__(self):
        return (
            f"Name: {self.name}, Salary: {self.salary}, "
            f"Dept: {self.department}, Lang: {self.programming_language}, "
            f"Team Size: {self.team_size}"
        )
