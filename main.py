kilo = int(input('Kilo: '))
# Kullanıcıdan kilo bilgisini alır
boy = float(input('Boy: '))
# Kullanıcıdan boy bilgisini alır
bke = kilo / (boy ** 2)
# Vücut Kitle İndeksi (VKİ) hesaplaması yapar
print(bke)
# VKİ değerini ekrana yazdırır
# VKİ'ye göre değerlendirme yapar ve sonucu ekrana yazdırır
if bke < 18.5:
    print('Zayıf')
elif 18.5 <= bke < 25:
    print('Normal')
elif 25 <= bke < 30:
    print('Fazla Kilolu')
elif bke >= 30:
    print('Obez')

