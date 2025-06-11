# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
from operator import index

people_records: list[tuple[str, str, int, str, str]] = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
my_record: tuple[str | int, ...] = ('Den', 'Ko', 39, 'Q.A.', 'Kiev')
people_records.insert(0, my_record)

people_records[1], people_records[5] = people_records[5], people_records[1]
index_to_check: tuple[int, ...] = (6, 10, 13)

for record in index_to_check:
    person = people_records[record]
    print(person, ">=30?", person[2] >= 30, "\n")

all_above_30: bool = all(people_records[record][2] >= 30 for record in index_to_check)
print(f"Результат перевірки, чи всім по 30 років: {all_above_30}")
