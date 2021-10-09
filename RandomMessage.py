import requests

url = "https://ai-chatbot.p.rapidapi.com/chat/free"

prevMsg = "Did you ever eat pizza?"  # change this to the actual previous message

querystring = {"message": prevMsg, "uid": ":)"}

headers = {
    'x-rapidapi-host': "ai-chatbot.p.rapidapi.com",
    'x-rapidapi-key': "api key goes here"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
