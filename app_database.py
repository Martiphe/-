import sqlite3 as sql

con = sql.connect('academic_performance.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS students (
     name TEXT, 
     grade TEXT
)""")
con.commit()

student_name = input('Фамилия и имя студента: ')
student_grade = input('Зачёт: ')
a = student_grade
cur.execute("SELECT * FROM students WHERE name=?", (student_name,))

if cur.fetchone() is None:
    cur.execute("INSERT INTO students VALUES(?, ?)",(student_name,student_grade))
    con.commit()
    cur.execute("SELECT * FROM students")
    print('Успеваемость')
    for value in cur.execute("SELECT * FROM students"):
        print(value)
else:
    for value in cur.execute("SELECT * FROM students WHERE name=?", (student_name,)):
        cur.execute("UPDATE students SET grade = ? where name =?", (student_grade,student_name))
        con.commit()
        for value in cur.execute("SELECT * FROM students"):
            print(value)

con.close())


