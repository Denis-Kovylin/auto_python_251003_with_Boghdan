import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from client.image_client import ImageApiClient

client = ImageApiClient()
filename = "test_image.jpg"
local_path = os.path.join("images", filename)


def test_upload_image():
    url = client.post_upload_image(local_path)
    assert url.startswith("http://127.0.0.1:8080/uploads/")
    assert filename in url


def test_get_image_url_json():
    url = client.get_image_url(filename, as_image=False)
    assert url.endswith(f"/uploads/{filename}")


def test_get_image_bytes():
    content = client.get_image_url(filename, as_image=True)
    assert isinstance(content, bytes)
    assert len(content) > 100  # картинка не может быть пустой


def test_delete_image():
    msg = client.delete_image(filename)
    assert "deleted" in msg.lower()
