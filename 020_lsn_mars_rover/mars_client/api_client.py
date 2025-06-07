import os
import requests


class NasaApiClient:
    BASE_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

    def __init__(self, api_key: str = "DEMO_KEY"):
        self.session = requests.Session()
        self.api_key = api_key

    def get_photos(self, sol: int = 1000, camera: str = "fhaz") -> list:
        params = {
            "sol": sol,
            "camera": camera,
            "api_key": self.api_key
        }

        response = self.session.get(self.BASE_URL, params=params)
        response.raise_for_status()  # выбросит ошибку, если что-то не так

        data = response.json()
        return data.get("photos", [])
