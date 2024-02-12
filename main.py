from requests import request
from dotenv import load_dotenv
import telebot
import os
import time
import logging
from images import get_random_image

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    filename = "mylog.log")


token = os.getenv("TOKEN_BOT")
chat_id = os.getenv("CANNEL_ID")


def publish_images(token: str, chat_id: str):
    """Публикует картинки в канал.

    Args:
        token (str): токен телеграм бота
        chat_id (str): уникальный идентификатор целевого чата или имя пользователя целевого канала (в формате @channelusername)
    """
    bot = telebot.TeleBot(token=token)
    counter = 0
    while counter != 123:
        image_foxes = get_random_image()
        for image in image_foxes:
            bot.send_photo(chat_id=chat_id, photo=image)
            # 86400
            time.sleep(10)
            counter += 1


def check_env() -> bool:
    """Проверка переменныъх в .env"""
    with open(".env", "r") as file:
        readed_file = file.read()
        res = readed_file.split("\n")

    checked_variables = ["TOKEN_BOT", "CANNEL_ID"]
    res_keys = [res_str.split("=")[0] for res_str in res if len(res_str) > 1]
    for key in checked_variables:
        if not key in res_keys:
            return False
        for env_str in res:
            splitted_str = env_str.split("=")
            if key == splitted_str[0]:
                if len(splitted_str) < 2:
                    return False
    return True


def main():
    if not check_env():
        print("не хватает переменных")
    publish_images(token=token, chat_id=chat_id)


if __name__ == "__main__":
    main()
