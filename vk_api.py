import logging
import os

import requests
from dotenv import load_dotenv

from images import get_random_image

load_dotenv()


def get_server_address() -> str:
    """Получает адрес сервера для загрузки картинки на стену сообщества"""
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {
        "access_token": os.getenv("ACCESS_TOKEN"),
        "v": "5.131",
        "group_id": os.getenv("GROUP_ID"),
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response = response.json()
    server_address = response["response"]["upload_url"]
    return server_address


def transfer_image_server(server_address: str):
    """Передача картинки на сервер"""
    image = get_random_image()
    response = requests.post(server_address, files={"file": ("filename.jpg", image)})
    response.raise_for_status()
    response = response.json()
    server = response["server"]
    photo = response["photo"]
    hash_vk = response["hash"]
    return server, photo, hash_vk


def save_photo_on_server(server, photo, hash_vk):
    """Сохранение картинки на сервере"""
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        "access_token": os.getenv("ACCESS_TOKEN"),
        "v": "5.131",
        "group_id": os.getenv("GROUP_ID"),
        "photo": photo,
        "server": server,
        "hash": hash_vk,
    }
    response = requests.post(url=url, params=params)
    response.raise_for_status()
    response = response.json()
    photo_id = response["response"][0]["id"]
    owner_id = response["response"][0]["owner_id"]
    return photo_id, owner_id


def publish_image_vk(photo_id, owner_id):
    """Публикация картинки на стене"""

    url = "https://api.vk.com/method/wall.post"
    params = {
        "access_token": os.getenv("ACCESS_TOKEN"),
        "v": "5.131",
        "from_group": 1,
        "attachments": f"photo{owner_id}_{photo_id}",
        "owner_id": f"-{os.getenv('GROUP_ID')}",
    }
    response = requests.post(url=url, params=params)
    response.raise_for_status()
    response = response.json()
    post_id = response["response"]["post_id"]
    if post_id:
        logging.info("Картинка опубликована")
    else:
        raise ValueError("Картинка не опубликована")


if __name__ == "__main__":
    server_address = get_server_address()
    server, photo, hash_vk = transfer_image_server(server_address)
    photo_id, owner_id = save_photo_on_server(
        server=server, photo=photo, hash_vk=hash_vk
    )
    publish_image_vk(photo_id=photo_id, owner_id=owner_id)
