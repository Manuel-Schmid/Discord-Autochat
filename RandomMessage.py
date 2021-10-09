import requests

url = "https://ai-chatbot.p.rapidapi.com/chat/free"

prevMsg = "Did you ever eat pizza?"  # change this to the actual previous message

querystring = {"message": prevMsg, "uid": ":)"}

headers = {
    'x-rapidapi-host': "ai-chatbot.p.rapidapi.com",
    'x-rapidapi-key': "3237f4b0e3msh63eba00f657ab8fp11a6b7jsncbd40131ab67"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
