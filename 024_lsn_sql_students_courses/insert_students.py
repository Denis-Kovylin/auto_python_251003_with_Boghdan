import sqlite3

students = [
    ("Harry", "Potter", "harry.potter@hogwarts.edu"),
    ("Hermione", "Granger", "hermione.granger@hogwarts.edu"),
    ("Ron", "Weasley", "ron.weasley@hogwarts.edu"),
    ("Draco", "Malfoy", "draco.malfoy@hogwarts.edu"),
    ("Luna", "Lovegood", "luna.lovegood@hogwarts.edu"),
    ("Neville", "Longbottom", "neville.longbottom@hogwarts.edu"),
    ("Ginny", "Weasley", "ginny.weasley@hogwarts.edu"),
    ("Cho", "Chang", "cho.chang@hogwarts.edu"),
    ("Cedric", "Diggory", "cedric.diggory@hogwarts.edu"),
    ("Fred", "Weasley", "fred.weasley@hogwarts.edu"),
    ("George", "Weasley", "george.weasley@hogwarts.edu"),
    ("Seamus", "Finnigan", "seamus.finnigan@hogwarts.edu"),
    ("Dean", "Thomas", "dean.thomas@hogwarts.edu"),
    ("Parvati", "Patil", "parvati.patil@hogwarts.edu"),
    ("Padma", "Patil", "padma.patil@hogwarts.edu"),
    ("Lavender", "Brown", "lavender.brown@hogwarts.edu"),
    ("Pansy", "Parkinson", "pansy.parkinson@hogwarts.edu"),
    ("Vincent", "Crabbe", "vincent.crabbe@hogwarts.edu"),
    ("Gregory", "Goyle", "gregory.goyle@hogwarts.edu"),
    ("Blaise", "Zabini", "blaise.zabini@hogwarts.edu")
]

conn = sqlite3.connect("hogwarts.db")
cursor = conn.cursor()

cursor.executemany(
    "INSERT INTO students (first_name, last_name, email) VALUES (?, ?, ?)",
    students
)

conn.commit()
conn.close()

print("✅ Students inserted successfully.")
