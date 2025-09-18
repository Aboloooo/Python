import os

counter = 0

while True:
    counter += 1
    os.remove(f"/Users/admin/Documents/SQL_Python_test/{counter}_test.txt")
    if counter == 5:
        break
