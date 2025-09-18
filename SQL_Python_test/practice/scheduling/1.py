import time

def task():
    print('Hi, we are testing')

start = time.time()
end = 6

while True:
    task()
    time.sleep(1)
    if time.time() - start > 6:
        print('task ends')
        break
