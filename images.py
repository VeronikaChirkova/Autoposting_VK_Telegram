import logging

import requests


def get_random_image() -> bytes:
    """Получает случайную картинку лис"""
    url = "https://randomfox.ca/floof"
    response = requests.get(url=url, verify=False)
    response.raise_for_status()
    logging.debug(response.status_code)
    response = response.json()
    image: bytes = requests.get(response["image"]).content
    return image


if __name__ == "__main__":
    get_random_image()
