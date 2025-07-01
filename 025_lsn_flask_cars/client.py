import requests
from requests.auth import HTTPBasicAuth
from logger import logger


class CarApiClient:
    def __init__(self, base_url: str):
        self.session = requests.Session()
        self.base_url = base_url

    def authenticate(self, username: str, password: str) -> None:
        auth_url = f"{self.base_url}/auth"
        response = self.session.post(auth_url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        token = response.json()["access_token"]
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        logger.info("🔐 Authenticated and token stored in session")

    def get_cars(self, sort_by: str = None, limit: int = None):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit
        response = self.session.get(f"{self.base_url}/cars", params=params)
        response.raise_for_status()
        return response.json()
