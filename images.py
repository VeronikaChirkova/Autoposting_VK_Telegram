import logging

import requests


def get_random_image() -> str:
    """Получает случайную картинку лис"""
    url = "https://randomfox.ca/floof"
    response = requests.get(url=url)
    response.raise_for_status()
    logging.debug(response.status_code)
    response = response.json()
    return response["image"]


if __name__ == "__main__":
    get_random_image()