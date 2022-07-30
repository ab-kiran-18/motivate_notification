import time
from turtle import title
from urllib import response
from plyer import notification
import requests

if __name__ == '__main__':
    k = []
    try:
        response = requests.get("https://zenquotes.io/api/quotes")
    except:
        notification.notify(
            title = 'error occurred',
            message = 'request to API is denied :( '
        )
    k = response.json()
    while True:
        for i in k:
            notification.notify(
            title = '''Today's motinoti...''',
            message = i['q'] +'\n'+'-- by '+ i['a'],
            timeout = 15
            )
            time.sleep(60)