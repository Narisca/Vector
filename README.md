# Vector
Programı yaparken ki amacım sitelerde paylaşılan resim dosyaları üzerinden kullanıcı isimlerini toplamaktı. Bu sayede belirli protokollere veyahut giriş formlarına kör deneme yanılma saldırısı yapmaktansa en azından elde ettiğim kullanıcı isimleri ile daha iyi bir saldırı gerçekleştirebilecektim. Bunun yanı sıra sadece kullanıcı isimlerini toplamak yerine diğer bilgileri de toplamanın bana daha fazla bilgi sağlayacanı düşündüm ve bu yüzden kullanıcı adlarının dışında bulabildiği tüm exif verilerini kayıt etmesini istedim.

Bahsettiğim olaya ilişkin bir olayı buradan görüntüleyebilirsiniz: https://www.youtube.com/watch?v=rfAmMQV_wss&t=255

## Programın indirilmesi ve kurulması
```markdown
git clone https://github.com/Narisca/Vector/
cd Vector
pip3 install -r requirements.txt
```

bu komutları kullanarak programı indirip kurduktan sonra `python3 vector.py --help` komutunu kullanarak programı nasıl çalıştırabileceğinizi öğrenebilirsiniz.

![1](https://github.com/Narisca/Vector/assets/165813191/419ef918-5f38-4f21-a5e6-0315672820fb)

## Örnek kullanım

```
python3 vector --url https://hedef.com/ --crawl 2 --keywords "author,owner name,artist"
```

```markdown
--url, -u     : Bu parametre hedef siteyi belirtmenizi sağlar.
--crawl, -c   : Bu parametre inilecek en derin alanı belirtmenizi sağlar. Örneğin 1 derinliği ana sayfayı kapsarken, 2 derinliği ana sayfada ki linklerin içeriğini de kapsar.
--keywords -k : Bu parametre toplanmasını istediğiniz exif verilerini belirtmenizi sağlıyor. Örneğin: software,author,model,copyright.. 
```
