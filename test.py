from PIL import Image
from PIL.ExifTags import TAGS
import requests
from io import BytesIO

image = Image.open("1.jpg")
exif_data = image.getexif()
print(exif_data)
exit()
if exif_data:
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        print(str(tag) + " " + str(value))