import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    
    # Rastgele bir sayı seçelim (1 ile 100 arasında)
    hedef_sayi = random.randint(1, 100)
    
    while True:
        try:
            tahmin = int(input("Bir sayı tahmin edin (1 ile 100 arasında): "))
        except ValueError:
            print("Geçerli bir sayı giriniz.")
            continue

        if tahmin < 1 or tahmin > 100:
            print("Lütfen 1 ile 100 arasında bir sayı girin.")
            continue

        if tahmin < hedef_sayi:
            print("Daha büyük bir sayı deneyin.")
        elif tahmin > hedef_sayi:
            print("Daha küçük bir sayı deneyin.")
        else:
            print(f"Tebrikler! Doğru tahmin ettiniz. Hedef sayı: {hedef_sayi}")
            break

if __name__ == "__main__":
    sayi_tahmin_oyunu()
