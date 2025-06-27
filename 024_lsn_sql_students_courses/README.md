```markdown
# Hogwarts Student-Course Database

📚 This project implements a student-course management system using SQLite and Python, set in the Harry Potter universe.

## 🧱 Project Structure

```

├── hogwarts.db # SQLite database file
├── init_schema.sql # SQL schema for tables: students, courses, enrollments
├── create_tables.py # Creates the tables from init_schema.sql
├── insert_courses.py # Inserts 5 Hogwarts courses
├── insert_students.py # Inserts 20 students
├── enroll_students.py # Randomly assigns students to 1–3 courses
├── check_courses.py # Console output to verify courses in DB
├── check_students.py # Console output to verify students in DB
├── check_enrollments.py # Console output to verify student-course assignments
├── hogwarts_crud.py # Class with CRUD operations on students and enrollments
├── crud_usage.py # Usage example for HogwartsCRUD class
├── requirements.txt # (Optional) Python dependencies, empty or minimal

```

## 🗃️ Database Schema

### `students` table
- `id` INTEGER (Primary Key)
- `first_name` TEXT (Not Null)
- `last_name` TEXT (Not Null)
- `email` TEXT (Unique, Not Null)

### `courses` table
- `id` INTEGER (Primary Key)
- `name` TEXT (Not Null)
- `description` TEXT (Optional)

### `enrollments` table
Many-to-many relation between students and courses:
- `student_id` INTEGER (Foreign Key → students.id)
- `course_id` INTEGER (Foreign Key → courses.id)

## 🚀 How to Run

1. **Create the database and tables**
   ```bash
   python create_tables.py
   ```

2. **Insert initial data**
   ```bash
   python insert_courses.py
   python insert_students.py
   ```

3. **Enroll students in courses**
   ```bash
   python enroll_students.py
   ```

4. **Check database content**
   ```bash
   python check_courses.py
   python check_students.py
   python check_enrollments.py
   ```

5. **Test CRUD operations**
   ```bash
   python crud_usage.py
   ```

## 🧪 CRUD Functionalities

Implemented in `hogwarts_crud.py`:

- Add new student and enroll in course
- Update student details
- View all courses for a student
- View all students in a course
- Delete student (with cleanup from enrollments)

## ✅ Dependencies

```bash
Python 3.10+ (no external packages required)
```

## 🧙‍♂️ Example: CRUD Output

```text
✅ Student Tom Riddle added and enrolled in course: Defense Against the Dark Arts
✅ Student Tom Riddle updated (email)
📚 Courses for Tom Riddle: ['Defense Against the Dark Arts']
🧑‍🎓 Students in course Defense Against the Dark Arts: ['Blaise Zabini', 'Cedric Diggory', 'Cho Chang', 'Ginny Weasley', 'Gregory Goyle', 'Harry Potter', 'Padma Patil', 'Pansy Parkinson', 'Seamus Finnigan', 'Vincent Crabbe', 'Tom Riddle']
❌ Student Tom Riddle deleted from database
```

## 📝 Notes

- You can safely delete and recreate `hogwarts.db` to reset the state.
- The project uses only SQLite and the built-in Python modules — no need to install anything via pip.
- To test in PyCharm, run files individually using the green play button or terminal.

---
Made with ❤️ by a Hogwarts alumnus and an AI owl.

```
