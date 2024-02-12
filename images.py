import requests


def get_random_image():
    """Получает список случайных картинок лис.
    """

    url = "https://randomfox.ca/floof"
    response = requests.get(url=url)
    response.raise_for_status()
    response = response.json()

    images_foxes = []
    random_image_url = response['image']
    images_foxes.append(random_image_url)
    return images_foxes