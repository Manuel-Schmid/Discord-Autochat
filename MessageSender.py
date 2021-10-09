import requests

# https://discord.com/api/v9/channels/700261153690877976/messages

payload = {
    'content': "hello world"
}

header = {
    'authorization': 'token goes here'
}

r = requests.post("https://discord.com/api/v9/channels/700261153690877976/messages", data=payload, headers=header)
