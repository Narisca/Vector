from .helpers import *
from .crawler import crawlerMain
from .exif import getData

def start():
    print_logo()
    args = ArgumentParser()
    
    info("Hedef sitede üzerinden linker toplanıyor...")
    images = crawlerMain(args.url, args.crawl)

    info("Exif verileri toplanıyor...")
    data = getData(images, args.keywords)

    x = [str(item[0]) for item in data]
    
    for i in x:
        with open("results/" + i + ".txt", "a") as file:
            for item in data:
                if i == str(item[0]):
                    file.write(str(item[1]) + "\n")

    info(f"{len(data)} adet veri results/ klasörüne kayıt edildi.")