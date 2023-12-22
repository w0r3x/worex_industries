import yazitura
import tkm
import sayıtahmin
import worexbilmece

def gamemenu():
    print("╔─────────────────────────╗")
    print("|     \033[91mWorex Industries\033[0m    |")
    print("|                         |")
    print("| 1- Yazı - Tura          |")
    print("| 2- Taş - Kağıt - Makas  |")
    print("| 3- Sayı Tahmin          |")
    print("| 4- Bilmece              |")
    print("| 5- *Çıkış*              |")
    print("╚─────────────────────────╝")

    secim = input("Lütfen Seçim Yapın.")

    if secim == "1":
        yazitura.worexyazitura()
        gamemenu()
    elif secim == "2":
         tkm.tas_kagit_makas_oyunu()
         gamemenu()
    elif secim == "3":
        sayıtahmin.sayi_tahmin_oyunu()
        gamemenu()
    elif secim == "4":
        worexbilmece.worexbilir()
        gamemenu()  
    elif secim == "5":
        print("\033[91m")
        print("")                             


