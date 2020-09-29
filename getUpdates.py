import requests
import json
TOKEN = '1264159149:AAGLITr-bj-rC1wpFINhyOAbKQ6uJSFNqLs'
url =requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
def sendMessage(res, text):
    global response
    url1 = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    parameter = {
        'chat_id': res,
        'text': text
    }
    response = requests.get(url=url1, params=parameter)
data=url.json()
res=data['result'][-1]['message']['from']['id']
i = 0
while i<2:
    
    i += 1
    sendMessage(res, f'Salom:{i}')