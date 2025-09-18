import schedule
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()

counter = 0
Path_For_Files = "/Users/admin/Documents/SQL_Python_test/practice/automation of daily task/createdFilesPlace"
def task():
    counter +=1
    open(f"{Path_For_Files}/{counter}.txt", "x")
            
schedule.every(5).seconds.do(task())

starting_time = time.time()
end_time = 15 #seconds

while True:
    schedule.run_pending()
    time.sleep(1)
    if time.time() - starting_time > end_time:
        print("time ends")
        break