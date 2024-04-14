# Vector
Programı yaparken ki amacım sitelerde paylaşılan resim dosyaları üzerinden kullanıcı adlarını toplamaktı. Bu sayede belirli protokollere veyahut giriş formlarına kör deneme yanılma saldırısı yapmaktansa en azından elde ettiğim kullanıcı adları ile daha iyi bir saldırı gerçekleştirebilecektim. Bunun yanı sıra sadece kullanıcı adlarını toplamak yerine diğer bilgileri de toplamanın bana daha fazla bilgi sağlayacanı düşündüm ve bu yüzden kullanıcı adlarının dışında bulabildiği tüm exif verilerini kayıt etmesini istedim.

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
