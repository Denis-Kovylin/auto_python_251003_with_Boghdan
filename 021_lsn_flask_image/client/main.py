import time
from requests import delete

from image_client import ImageApiClient

client = ImageApiClient()
image_url = client.post_upload_image("../images/test_image.jpg")
print("Завантажено:", image_url, "\n")
time.sleep(1)

filename = "test_image.jpg"
url_from_server = client.get_image_url(filename, as_image=False)
print("URL зображення (з JSON):", url_from_server, "\n")

img_bytes = client.get_image_url(filename, as_image=True)
try:
    with open("../images/downloaded.jpg", "wb") as f:
        f.write(img_bytes)
    print("Зображення успішно збережено як downloaded.jpg", "\n")
except Exception as e:
    print("Помилка при збереженні зображення:", "\n", e)

delete_result = client.delete_image(filename)
print("Результат видалення:", delete_result, "\n")
