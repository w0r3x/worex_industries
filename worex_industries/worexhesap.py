def worexh():
    print("╔─────────────────────────╗ ")
    print("║       \033[91mWorex Hesap\033[0m       ║")
    print("║                         ║")
    print("║ -1 Toplama              ║")
    print("║ -2 Çıkarma              ║")
    print("║ -3 Çarpma               ║")
    print("║ -4 Bölme                ║")
    print("║ -5 Karekök              ║")
    print("║ -6 Üs Alma              ║")
    print("║ -7 Faktöriyel           ║")
    print("║ -8 Çıkış                ║")
    print("╚─────────────────────────╝")

    secim = input("Lütfen bir işlem seçin (1-8): ")

    if secim == "1":
        topla()
    elif secim == "2":
        cikar()
    elif secim == "3":
        carp()
    elif secim == "4":
        bol()
    elif secim == "5":
        karekok()
    elif secim == "6":
        us_alma()
    elif secim == "7":
        faktoriyel()
    elif secim == "8":
        print("Çıkış yapılıyor. İyi günler!")
    else:
        print("Geçersiz seçim. Lütfen 1 ile 8 arasında bir sayı girin.")

def topla():
    tbir = float(input("Lütfen birinci değeri girin: "))
    tiki = float(input("Lütfen ikinci değeri girin: "))
    print("Sonuç: ", tbir + tiki)

def cikar():
    cbir = float(input("Lütfen birinci değeri girin: "))
    ciki = float(input("Lütfen ikinci değeri girin: "))
    print("Sonuç: ", cbir - ciki)

def carp():
    cbir = float(input("Lütfen birinci değeri girin: "))
    ciki = float(input("Lütfen ikinci değeri girin: "))
    print("Sonuç: ", cbir * ciki)

def bol():
    cbir = float(input("Lütfen birinci değeri girin: "))
    ciki = float(input("Lütfen ikinci değeri girin: "))
    
    if ciki != 0:
        print("Sonuç: ", cbir / ciki)
    else:
        print("Bir sayıyı sıfıra bölemezsiniz!")

def karekok():
    sayi = float(input("Karekök almak istediğiniz sayıyı girin: "))
    print("Sonuç: ", math.sqrt(sayi))

def us_alma():
    taban = float(input("Tabanı girin: "))
    us = float(input("Üssü girin: "))
    print("Sonuç: ", taban ** us)

def faktoriyel():
    sayi = int(input("Faktöriyelini almak istediğiniz sayıyı girin: "))
    print("Sonuç: ", math.factorial(sayi))
