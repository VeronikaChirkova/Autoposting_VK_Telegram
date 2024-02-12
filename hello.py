import requests
import time
from requests import request
from dotenv import load_dotenv
import telebot
import os
import time
from images import get_random_image

load_dotenv()

token = os.getenv("TOKEN_BOT")
chat_id = os.getenv("CANNEL_ID")

def get_random_image():
    """Получает список случайных картинок лис.
    """
    images_foxes = []
    url = "https://randomfox.ca/floof"
    response = requests.get(url=url)
    response.raise_for_status()
    response = response.json()
    random_image_url = response['image']
    images_foxes.append(random_image_url)
    return images_foxes
    # print(images_foxes)


# def get_random_image():
#     """Получает список случайных картинок лис.
#     """
#     url = "https://randomfox.ca/floof"
#     images_foxes = []
#     counter = 0
#     while counter < 10:
#         response = requests.get(url=url)
#         response.raise_for_status()
#         response = response.json()
#         random_image_url = response['image']
#         images_foxes.append(random_image_url)
#         counter += 1
#     return images_foxes
def publish_images(token: str, chat_id: str):
    """Публикует картинки в канал.

    Args:
        token (str): токен телеграм бота
        chat_id (str): уникальный идентификатор целевого чата или имя пользователя целевого канала (в формате @channelusername)
    """
    bot = telebot.TeleBot(token=token)
    image_foxes = get_random_image()
    for image in image_foxes:
        bot.send_photo(chat_id=chat_id, photo=image, caption="Fox")
        time.sleep(10)

publish_images(token=token, chat_id="-1002052983324")