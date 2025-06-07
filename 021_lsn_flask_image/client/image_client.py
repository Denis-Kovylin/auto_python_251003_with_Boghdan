import os
import requests
from typing import Union


class ImageApiClient:
    def __init__(self, base_url="http://127.0.0.1:8080"):
        self.base_url = base_url
        self.session = requests.Session()

    def post_upload_image(self, image_path: str) -> str:
        url = f"{self.base_url}/upload"

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл {image_path} не знайдено")

        with open(image_path, "rb") as img:
            files = {"image": img}
            response = self.session.post(url, files=files)
            response.raise_for_status()

        data = response.json()
        return data["image_url"]

    def get_image_url(self, filename: str, as_image: bool = False) -> Union[str, bytes]:
        headers = {
            "Content-Type": "image" if as_image else "text"
        }

        url = f"{self.base_url}/image/{filename}"
        response = self.session.get(url, headers=headers)
        response.raise_for_status()

        if as_image:
            return response.content
        else:
            data = response.json()
            return data.get("image_url")

    def delete_image(self, filename: str) -> str:
        url = f"{self.base_url}/delete/{filename}"
        response = self.session.delete(url)
        response.raise_for_status()

        data = response.json()
        return data.get("message", "Файл видалено")
