import pytest
from client import CarApiClient
from logger import logger


@pytest.fixture(scope="class")
def api_client():
    client = CarApiClient("http://127.0.0.1:8080")
    client.authenticate("test_user", "test_pass")
    return client


@pytest.mark.parametrize("sort_by,limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 10),
    ("brand", 7),
    (None, 4),
    ("price", None),
    (None, None),
])
def test_search_cars(api_client, sort_by, limit):
    logger.info(f"🚀 Testing GET /cars with sort_by={sort_by}, limit={limit}")
    cars = api_client.get_cars(sort_by=sort_by, limit=limit)
    assert isinstance(cars, list)
    if limit:
        assert len(cars) <= limit
