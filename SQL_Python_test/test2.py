import sqlite3
import os
from sqlite3 import OperationalError

conn = sqlite3.connect(':memory:')
c = conn.cursor()

sql_file_path = '/Users/admin/Documents/SQL_Python_test/tables2.sql'

with open(sql_file_path, 'r') as f:
    sql_script = f.read()

sqlCommands = sql_script.split(';')

for command in sqlCommands:
    command = command.strip()
    if command:
       try:
           c.execute(command)
       except OperationalError as msg :
           print('Command skipped: ', msg)

try:
    res = c.execute('SELECT * FROM Sites')
    print(res.fetchall())
except OperationalError as msg:
    print("Query failed:", msg)

conn2 = sqlite3.connect('conn2.db')
conn2


print(os.getcwd())
