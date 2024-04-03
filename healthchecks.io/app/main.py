import time
import requests
import schedule

print("App started")

def job():
    print('Sending heartbeat')
    res = requests.get('https://hc-ping.com/2f1d38ad-2606-4da0-8299-21e1c9c49ad0')
    if res.status_code != 200:
        print(f'{res.status_code} Error sending heartbeat: {res.text}')

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(15)