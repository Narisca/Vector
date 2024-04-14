from .helpers import success, info
from warnings import filterwarnings
from bs4 import BeautifulSoup
import requests

filterwarnings("ignore", category=UserWarning, module="bs4")

def format_link(link, item):
    if item.startswith("/"):
        target = link.split('/')[0] + "//" + link.split('/')[2] + item
        return target

    elif item.startswith("http"):
        if link.split('/')[2] in item:
            return item
    else:
        if not link.endswith("/"):
            link += "/"
        return link + item

def extension_check(link):
    if '.' in link:
        for extension in ["jpg", "png", "jpeg", "gif"]:
            if link.lower().endswith(extension):
                return True
    return False

def crawler(link):
    links = []
    images = []

    try:
        response = requests.get(link, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        })

        source = BeautifulSoup(response.content,"lxml")
        for item in source.find_all("a", href=True):
            item = item.get("href")

            if extension_check(item):
                image = format_link(link, item)
                if image not in images:
                    images.append(image)

            else:
                xlink = format_link(link, item)
                if xlink not in links:
                    links.append(xlink)

        for item in source.find_all("img"):
            item = item.get("src")

            if extension_check(item):
                image = format_link(link, item)
                if image not in images:
                    images.append(image)

    except KeyboardInterrupt:
        info("CTRL + C kombinasyonu kullanılarak programdan çıkış yapıldı.")
        exit()
    except:
        pass

    return links, images

def crawlerMain(url, count):
    allLinks = set()
    links = set()
    images = set()

    pages, pimages = crawler(url)
    images.update(pimages)
    
    success(f"{url} adresi üzerinden {str(len(pages))} link / {str(len(pimages))} resim toplandı.")

    for _ in range(count - 1):
        links.update(list(set(pages)))
        pages.clear()

        for link in list(set(links)):
            if link not in allLinks:
                x, pimages = crawler(link)
                images.update(pimages)

                pages.extend(x)
                allLinks.add(link)

                success(f"{link} adresi üzerinden {str(len(x))} link / {str(len(pimages))} resim toplandı.")

        links.clear()

    images = list(set(images))
    info(f"Toplam {str(len(images))} resim toplandı.")

    return images