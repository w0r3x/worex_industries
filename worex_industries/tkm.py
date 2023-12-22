import tkm
import random

def tas_kagit_makas_oyunu():
    print("Taş-Kağıt-Makas Oyununa Hoş Geldiniz!")

    while True:
        kullanici_secimi = input("Taş mı, Kağıt mı, Makas mı? (çıkış için 'q'): ").lower()

        if kullanici_secimi == 'q':
            print("Oyunu sonlandırdınız. İyi günler!")
            break

        if kullanici_secimi not in ['taş', 'kağıt', 'makas']:
            print("Geçerli bir seçenek giriniz: 'taş', 'kağıt' veya 'makas'.")
            continue

        bilgisayar_secimi = random.choice(['taş', 'kağıt', 'makas'])

        print(f"Bilgisayarın seçimi: {bilgisayar_secimi.capitalize()}")

        if kullanici_secimi == bilgisayar_secimi:
            print("Berabere! Tekrar deneyin.")
        elif (kullanici_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
             (kullanici_secimi == 'kağıt' and bilgisayar_secimi == 'taş') or \
             (kullanici_secimi == 'makas' and bilgisayar_secimi == 'kağıt'):
            print("Tebrikler! Kazandınız.")
        else:
            print("Üzgünüm! Kaybettiniz.")
