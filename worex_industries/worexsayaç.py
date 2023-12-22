from datetime import datetime, timedelta

def gun_sayaci():
    try:
        gun_sayisi = int(input("Kaç gün sonrasını öğrenmek istiyorsunuz: "))
        if gun_sayisi < 0:
            print("Geçerli bir gün sayısı giriniz.")
            return

        bugun = datetime.now()
        gelecek_tarih = bugun + timedelta(days=gun_sayisi)

        print(f"{gun_sayisi} gün sonra tarih: {gelecek_tarih.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Geçerli bir sayı giriniz.")
