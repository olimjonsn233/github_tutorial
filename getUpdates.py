import requests
import json
r=requests.get('https://api.telegram.org/bot1264159149:AAGLITr-bj-rC1wpFINhyOAbKQ6uJSFNqLs/getUpdates')
data=r.json()
yangilanganid=data['result'][0]['update_id']
fromm=data['result'][0]['message']['from']
chat=data['result'][0]['message']['chat']
print(yangilanganid)
print(fromm)
print(chat)
