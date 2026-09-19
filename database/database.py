# SQL - structured query language
# data - данные
# SQLite, PostreSQL, MySQL, MSSQL
import sqlite3

def create_tables(conn):
    # делаем SQL запрос для создания таблицы students
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            name TEXT,
            age INTEGER,
            city TEXT
        )
    """)

def add_student(conn, name, age, city):
    # печатаем данные студента в консоль (для наглядности)
    print(name, age, city)
    # запрос чтобы добавить данные студента в таблицу students
    conn.execute("""
    INSERT INTO students 
    VALUES (?, ?, ?)
    """,
    (name, age, city)
    )
    # Сохраняем добавленного студента в базе данных.
    conn.commit()

if __name__ == "__main__":
    # Файл database.db будет создан, если его ещё нет.
    connection = sqlite3.connect("database.db")
    # создаём таблицу students
    create_tables(connection)
    # добавляем студентов
    add_student(connection, "igor", 35, "Bishkek")
    add_student(connection, "daniyar", 36, "Naryn")
    # закрываем соединение с базой данных
    connection.close()
