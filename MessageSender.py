import requests
import time

# https://discord.com/api/v9/channels/700261153690877976/messages

payload = {
    'content': "hello world"
}

header = {
    'authorization': 'auth goes here'
}

for i in range(5):
    payload = {
        'content': "hello world " + str(i + 1)
    }
    r = requests.post("https://discord.com/api/v9/channels/700261153690877976/messages", data=payload, headers=header)
    time.sleep(2)  # 3 second delay
