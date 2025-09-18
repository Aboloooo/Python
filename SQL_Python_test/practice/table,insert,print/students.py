import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect(':memory:')
c = conn.cursor()

sql_file_path = '/Users/admin/Documents/SQL_Python_test/practice/1/students.sql'

with open(sql_file_path) as f:
    sql_commands = f.read()

sql_script = sql_commands.split(';')

for command in sql_script:
    command = command.strip()
    if command:
        try:
            c.execute(command)
        except OperationalError as msg:
            print('Command skipped:', msg) 

try:
    Class_Room_data = [
        (1,'A101', 'Building A'),
        (2,'B202', 'Building B'),
        (3,'C303', 'Building C'),
    ]
    Teacher_data = [
        (1,'Alice', 'Smith', 'Grade 1', 30),
        (2,'Bob', 'Johnson', 'Grade 2', 45),
        (3,'Charlie', 'Williams', 'Grade 3', 39),
    ]
    student_data = [
    (1,'Emma', 'Brown', 'Grade 1', 6, 1),
    (2,'Liam', 'Davis', 'Grade 2', 7, 2),
    (3,'Olivia', 'Miller', 'Grade 3', 8, 3),
    (4,'Noah', 'Wilson', 'Grade 1', 6, 1),
    (5,'Sophia', 'Moore', 'Grade 2', 7, 2),
    ]
    subject_data = [
    (1,'Math', 1, 1),
    (2,'Science', 2, 2),
    (3,'History', 3, 3),
    ]

    c.executemany("insert into ClassRoom values(?,?,?)" , Class_Room_data)
    c.executemany('insert into Teacher values(?,?,?,?,?)' , Teacher_data)
    c.executemany('insert into student values(?,?,?,?,?,?)' , student_data)
    c.executemany('insert into subject values(?,?,?,?)' , subject_data)

    conn.commit()

    # res = c.execute('SELECT subject_name FROM subject natural join Teacher where Teacher_ID = (SELECT Teacher_ID FROM Teacher where F_name="Alice")')
    # print(res.fetchall())
    for row in c.execute('SELECT subject_name FROM subject'):
        print(row)
except OperationalError as msg:
    print('Quary failed: ', msg)



