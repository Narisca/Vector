from .helpers import success, error, info
from PIL import Image
from PIL.ExifTags import TAGS
import requests
from io import BytesIO

def getData(links, keywords):
    data = []

    for image_link in links:
        try:
            response = requests.get(image_link, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            })

            if response.status_code == 200 or response.status_code == 304:
                image = Image.open(BytesIO(response.content))
                exif_data = image.getexif()

                if exif_data:
                    for tag_id, value in exif_data.items():
                        
                        try:
                            tag = TAGS.get(tag_id, tag_id)
                            if keywords != "all":
                                if tag.lower() in keywords.split(','):
                                    if [tag, value] not in data:
                                        success(f"{image_link} - {str(tag)} / {str(value)}")
                                        data.append([tag, value])
                            else:
                                if [tag, value] not in data:
                                    success(f"{image_link} - {str(tag)} / {str(value)}")
                                    data.append([tag, value])
                        except:
                            continue
                else:
                    error(f"{image_link} - exif verisi bulunamadı.")
            else:
                error(f"{image_link} - resim linkine erişilemiyor.")

        except KeyboardInterrupt:
            info("CTRL + C kombinasyonu kullanılarak programdan çıkış yapıldı.")
            exit()
        except:
            pass

    return data