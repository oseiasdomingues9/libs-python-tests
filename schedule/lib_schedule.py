import schedule
import time

def check_table():
    print(schedule.get_jobs())

schedule.every(10).seconds.do(check_table)

while True:
    schedule.run_pending()
    time.sleep(1)
    
#https://github.com/dbader/schedule
    
