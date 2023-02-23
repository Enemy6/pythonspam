import requests
import time

cookie = ""

auth_response = requests.post("https://auth.roblox.com/v1/logout", headers={"cookie": f".ROBLOSECURITY={cookie}"})

if auth_response.status_code == 403:
    if "x-csrf-token" in auth_response.headers:
        token = auth_response.headers["x-csrf-token"]

headers = {
    "cookie": f".ROBLOSECURITY={cookie}",
    "x-csrf-token": token
}

data = {
    "userId": 12314048, # your user id
    "subject": "",
    "body": Hello there, Kreek AKA Forest. I am a hacker. I work with Terror3096 I can't say my username or it will get censored (because chat filter sucks)",
    "recipientId": 140258990 # recipient's user Id
}

while True:
    message_response = requests.post("https://privatemessages.roblox.com/v1/messages/send", headers=headers, data=data)

    if message_response.status_code == 429:
        print(message_response.json())
        time.sleep(60)
    if message_response.status_code == 403:
        import os 
        os.system('python bot.py')
    print(f"{message_response.json()} || {message_response.status_code}")
    time.sleep(2)
