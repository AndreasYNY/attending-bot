import schedule
import time
import subprocess
import datetime

def pergi():
    subprocess.run('python pergi.py')

def pulang():
    subprocess.run('python pulang.py')


dayl = datetime.date.today()
weekl = dayl.weekday()
if weekl == 5:
    print("nothing to do, go back sleep!")
if weekl == 6:
    print("gereja mint")
else:
    schedule.every().day.at("22:30").do(pergi)
    schedule.every().day.at("23:00").do(pulang)

while True:
    schedule.run_pending()
    time.sleep(1)