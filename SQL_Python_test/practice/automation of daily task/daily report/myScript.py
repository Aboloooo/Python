import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.Connection('D:\MyGitHub\Python\SQL_Python_test\practice\automation of daily task\daily report')
c = conn.cursor()

file_path = 'D:\MyGitHub\Python\SQL_Python_test\tables2.sql'

with open(file_path, 'r') as f:
    sql_commands = f.read()

sql_scripts = sql_commands.split(';')

for command in sql_scripts:
    command = command.strip()
    if command:
        try:
            c.execute(command)
        except OperationalError as msg:
            print('Command skipped: ', msg)
    else:
        command

            
