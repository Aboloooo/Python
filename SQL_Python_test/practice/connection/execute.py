""" Here we want to extract and compare latest information from a log file """

import mysql.connector

"""
here is the way I connect to the db with php
 $host = 'localhost';
$username = 'root';
$password = '';
$port = '3306';
$certificate_file_path = '';
$database = 'Lily_Undon'; """

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'Lily_Undon',
    port = 3306
)
c = conn.cursor()
""" c.execute('INSERT INTO AccessLevel (AccessLevelID, level) VALUES (20, "client")') """
c.execute('select * from Sites')

rows = c.fetchall()

for row in rows:
    print(row[1])