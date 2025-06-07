import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from mars_client.api_client import NasaApiClient


@pytest.fixture
def nasa_client():
    return NasaApiClient()


def test_get_photos_returns_list(nasa_client):
    photos = nasa_client.get_photos()
    assert isinstance(photos, list), "Ожидался список"
    assert len(photos) > 0, "Список фотографий пустой"


def test_photos_contain_expected_keys(nasa_client):
    photos = nasa_client.get_photos()
    sample = photos[0]
    assert "img_src" in sample, "Отсутствует ключ 'img_src'"
    assert sample["img_src"].startswith("http"), "Ссылка на фото невалидна"
