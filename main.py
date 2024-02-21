from email.mime import image
import logging
import os
import time

import telebot
from dotenv import load_dotenv

from images import get_random_image
from vk_api import (
    get_server_address,
    publish_image_vk,
    save_photo_on_server,
    transfer_image_server,
)

load_dotenv()

token = os.getenv("TOKEN_BOT")
chat_id = os.getenv("CHANNEL_ID")
DAY = 86400
image = get_random_image()


def publish_images(token: str, chat_id: str, interval: int):
    """Публикует картинки в телеграм канал

    Args:
        token (str): токен телеграм бота
        chat_id (str): уникальный идентификатор целевого чата или имя пользователя целевого канала (в формате @channelusername)
        interval (int): интервал между публикациями картинок в секундах
    """
    bot = telebot.TeleBot(token=token)
    while True:
        bot.send_photo(chat_id=chat_id, photo=image)
        time.sleep(interval)


def check_env() -> bool:
    """Проверка переменныъх в .env"""
    with open(".env", "r") as file:
        readed_file = file.read()
        res = readed_file.split("\n")

    checked_variables = [
        "TOKEN_BOT",
        "CHANNEL_ID",
        "CLIENT_ID",
        "ACCESS_TOKEN",
        "GROUP_ID",
    ]
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
    logging.basicConfig(
        level=logging.DEBUG if os.getenv("DEV") else logging.WARNING,
        format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
    )

    if not check_env():
        msg = "не хватает переменных в .env"
        logging.critical(msg)
        raise ValueError(msg)

    server_address = get_server_address()
    server, photo, hash_vk = transfer_image_server(server_address)
    photo_id, owner_id = save_photo_on_server(
        server=server, photo=photo, hash_vk=hash_vk
    )
    publish_image_vk(photo_id=photo_id, owner_id=owner_id)
    publish_images(token=token, chat_id=chat_id, interval=DAY)  # type:ignore


if __name__ == "__main__":
    main()
