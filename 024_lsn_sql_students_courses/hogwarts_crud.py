import sqlite3
from typing import Optional


class HogwartsCRUD:
    def __init__(self, db_name: str = "hogwarts.db") -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_student(self, first_name: str, last_name: str, email: str, course_id: int) -> None:
        self.cursor.execute(
            "INSERT INTO students (first_name, last_name, email) VALUES (?, ?, ?)",
            (first_name, last_name, email)
        )
        student_id = self.cursor.lastrowid

        self.cursor.execute("SELECT name FROM courses WHERE id = ?", (course_id,))
        course_name = self.cursor.fetchone()
        if course_name:
            self.cursor.execute(
                "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
                (student_id, course_id)
            )
            self.conn.commit()
            print(f"✅ Student {first_name} {last_name} added and enrolled in course: {course_name[0]}")
        else:
            print(f"❌ Course ID {course_id} not found.")

    def update_student(
            self,
            student_id: int,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            email: Optional[str] = None
    ) -> None:
        self.cursor.execute("SELECT first_name, last_name FROM students WHERE id = ?", (student_id,))
        student = self.cursor.fetchone()
        if not student:
            print(f"❌ Student ID {student_id} not found.")
            return

        original_name = f"{student[0]} {student[1]}"
        changes = []

        if first_name:
            self.cursor.execute("UPDATE students SET first_name = ? WHERE id = ?", (first_name, student_id))
            changes.append("first name")
        if last_name:
            self.cursor.execute("UPDATE students SET last_name = ? WHERE id = ?", (last_name, student_id))
            changes.append("last name")
        if email:
            self.cursor.execute("UPDATE students SET email = ? WHERE id = ?", (email, student_id))
            changes.append("email")

        self.conn.commit()
        print(f"✅ Student {original_name} updated ({', '.join(changes)})")

    def get_student_courses(self, student_id: int) -> None:
        self.cursor.execute(
            "SELECT first_name, last_name FROM students WHERE id = ?", (student_id,)
        )
        student = self.cursor.fetchone()
        if not student:
            print(f"❌ Student ID {student_id} not found.")
            return

        full_name = f"{student[0]} {student[1]}"
        self.cursor.execute(
            "SELECT courses.name FROM courses "
            "JOIN enrollments ON courses.id = enrollments.course_id "
            "WHERE enrollments.student_id = ?", (student_id,)
        )
        courses = self.cursor.fetchall()
        if courses:
            print(f"📚 Courses for {full_name}: {[course[0] for course in courses]}")
        else:
            print(f"ℹ️ {full_name} is not enrolled in any course.")

    def get_course_students(self, course_id: int) -> None:
        self.cursor.execute("SELECT name FROM courses WHERE id = ?", (course_id,))
        course = self.cursor.fetchone()
        if not course:
            print(f"❌ Course ID {course_id} not found.")
            return

        self.cursor.execute(
            "SELECT students.first_name, students.last_name FROM students "
            "JOIN enrollments ON students.id = enrollments.student_id "
            "WHERE enrollments.course_id = ?", (course_id,)
        )
        students = self.cursor.fetchall()
        if students:
            print(f"🧑‍🎓 Students in course {course[0]}: {[f'{s[0]} {s[1]}' for s in students]}")
        else:
            print(f"ℹ️ No students enrolled in {course[0]}.")

    def delete_student(self, student_id: int) -> None:
        self.cursor.execute("SELECT first_name, last_name FROM students WHERE id = ?", (student_id,))
        student = self.cursor.fetchone()
        if not student:
            print(f"❌ Student ID {student_id} not found.")
            return

        full_name = f"{student[0]} {student[1]}"
        self.cursor.execute("DELETE FROM enrollments WHERE student_id = ?", (student_id,))
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()
        print(f"❌ Student {full_name} deleted from database")

    def close(self) -> None:
        self.conn.close()
