import os
from mars_client.api_client import NasaApiClient

client = NasaApiClient()
photos = client.get_photos(sol=1000, camera="fhaz")

if not os.path.exists("images"):
    os.makedirs("images")

for index, photo in enumerate(photos, start=1):
    img_url = photo['img_src']
    img_response = client.session.get(img_url)

    file_name = f"mars_photo{index}.jpg"
    file_path = os.path.join("images", file_name)

    with open(file_path, "wb") as file:
        file.write(img_response.content)

    print(f"Фотокартку {index} збережено: {file_name}")
