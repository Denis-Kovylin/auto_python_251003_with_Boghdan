import pytest
from selenium import webdriver
from pathlib import Path


@pytest.fixture(scope="function")
def driver():
    # Путь до локального HTML-файла
    html_path = Path(__file__).parent / "html" / "dz.html"
    file_url = html_path.resolve().as_uri()

    # Настройка браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(file_url)

    yield driver

    driver.quit()
