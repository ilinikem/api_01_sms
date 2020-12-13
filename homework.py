import time
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
NUMBER_FROM = os.getenv('phone_from')
NUMBER_TO = os.getenv('phone_to')

client = Client(account_sid, auth_token)


def get_status(user_id):
    params = {
        "access_token": os.getenv('access_token'),
        "user_id": user_id,
        "v": "5.52",
        "fields": "online"
    }
    url = "https://api.vk.com/method/users.get"
    status = requests.get(url, params=params).json()['response']
    status_online = status[0]['online']
    return status_online


def sms_sender(sms_text):
    message = client.messages.create(
        to=NUMBER_TO,
        from_=NUMBER_FROM,
        body=sms_text)
    return print(message.sid)


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
