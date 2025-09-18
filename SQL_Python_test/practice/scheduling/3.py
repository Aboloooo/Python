import schedule
import time

def callMe():
    print('Hi, this msg is on repeat.')

schedule.every(2).seconds.do(callMe)

start_time = time.time()
ends_at = 5

while True:
    schedule.run_pending()
    if time.time() - start_time > ends_at:
        print('Schedule stops')
        break

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

    
    

