# SQL - structured query language
# data - данные
# SQLite, PostreSQL, MySQL, MSSQL
import sqlite3

def create_tables(conn):
    conn.execute("DROP TABLE IF EXISTS students")
    # делаем SQL запрос для создания таблицы students
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            city TEXT
        )
    """)

def add_student(conn, name, age, city):
    # печатаем данные студента в консоль (для наглядности)
    print(name, age, city)
    # запрос чтобы добавить данные студента в таблицу students
    conn.execute("""
    INSERT INTO students (name, age, city)
    VALUES (?, ?, ?)
    """,
    (name, age, city)
    )
    # не делаем через f-string дабы избежать sql-injection
    # Сохраняем добавленного студента в базе данных.
    conn.commit()

def get_all_students(conn):
    # result = conn.execute(
    #     "SELECT * FROM students"
    # )
    result = conn.execute(
        "SELECT age, name FROM students"
    )
    return result.fetchall()

def get_student(conn, student_id):
    result = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )
    return result.fetchone()


def get_students_by_city_and_age(conn, city, age):
    result = conn.execute(
        "SELECT * FROM students WHERE city = ? AND age < ?",
        (city, age)
    )
    return result.fetchall()

def delete_student_by_id(conn, student_id):
    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()

def change_age(conn, student_id, new_age):
    conn.execute(
        "UPDATE students SET age = ? WHERE id = ?",
        (new_age, student_id)
    )
    conn.commit()

def change_student(conn, name, age, city, student_id):
    conn.execute(
        """
        UPDATE students SET name = ?, age = ?, city = ?
        WHERE id = ?
        """,
        (name, age, city, student_id)
    )

if __name__ == "__main__":
    # Файл database.db будет создан, если его ещё нет.
    connection = sqlite3.connect("database.db")
    # создаём таблицу students
    create_tables(connection)
    print("добавляем студентов")
    add_student(connection, "Igor", 35, "Bishkek")
    add_student(connection, "Daniyar", 36, "Naryn")
    add_student(connection, "Anna", 20, "Bishkek")

    print("получаем студентов из таблицы")
    students = get_all_students(connection)
    for st in students:
        print(st)

    print("получаем одного студента по ID")
    print(get_student(connection, 2))

    print("получаем студентов по городу и возрасту")
    students = get_students_by_city_and_age(
        connection,
        "Bishkek",
    37
    )
    for st in students:
        print(st)

    print("удаляем студента")
    delete_student_by_id(connection, 1)
    print(get_all_students(connection))

    print("изменяем возраст студента")
    change_age(connection, 3, 25)
    print(get_student(connection, 3))

    # закрываем соединение с базой данных
    connection.close()
