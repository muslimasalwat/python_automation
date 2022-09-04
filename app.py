import requests
import schedule

import time 

def send_message():
    resp = requests.post('https://textbelt.com/text',{
        'phone': '+233558640598',
        'message':'Hello Muslima. Good Morning',
        'key': 'textbelt'
    })
    print (resp.json())

schedule.every().day.at("09:00").do(send_message)
#schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)