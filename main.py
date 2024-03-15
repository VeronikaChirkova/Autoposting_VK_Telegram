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

# ide run
load_dotenv()

token = os.getenv("TOKEN_BOT")
chat_id = os.getenv("CHANNEL_ID")
DAY = 86400


def publish_images(token: str, chat_id: str, interval: int, image: bytes):
    """Публикует картинки в телеграм канал

    Args:
        token (str): токен телеграм бота
        chat_id (str): уникальный идентификатор целевого чата или имя пользователя целевого канала (в формате @channelusername)
        interval (int): интервал между публикациями картинок в секундах
        image (bytes): картинка для загрузки в сервисы
    """
    bot = telebot.TeleBot(token=token)
    while True:
        bot.send_photo(chat_id=chat_id, photo=image)
        time.sleep(interval)


def check_env() -> bool:
    """Проверка переменныъхv в .env

    --env-file .env
    """
    checked_variables = [
        "TOKEN_BOT",
        "CHANNEL_ID",
        "CLIENT_ID",
        "ACCESS_TOKEN",
        "GROUP_ID",
    ]
    for env_var in checked_variables:
        token = os.getenv(env_var)
        if token is None:
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

    image = get_random_image()

    server_address = get_server_address()
    server, photo, hash_vk = transfer_image_server(server_address)
    photo_id, owner_id = save_photo_on_server(
        server=server, photo=photo, hash_vk=hash_vk
    )
    publish_image_vk(photo_id=photo_id, owner_id=owner_id)
    publish_images(
        token=token, chat_id=chat_id, interval=DAY, image=image  # type:ignore
    )


if __name__ == "__main__":
    main()
