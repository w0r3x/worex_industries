def iletisim_menu():
    while True:
        print("\033[91m===============================")
        print("|      Worex Industries       |")
        print("===============================\033[0m")
        print("╔─────────────────────────╗")
        print("|  Worex İletişim Menüsü  |")
        print("|                         |")
        print("| 1- İletişim Bilgileri   |")
        print("| 2- Benim Hakkımda       |")
        print("| 3- Ana Menü             |")
        print("╚─────────────────────────╝")

        secim = input("Lütfen bir işlem seçin (1-3): ")

        if secim == "1":
            iletisim_bilgileri_goster()
        elif secim == "2":
            hakkimda_bilgileri_goster()
        elif secim == "3":
            print("Ana Menüye dönülüyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 ile 3 arasında bir sayı girin.")

def iletisim_bilgileri_goster():
    print("İletişim Bilgileri:")
    print("- E-posta: worex_long@mail.com")
    print("- İnstagram: uva_applic")
    print("- Telefon: Belirtmeyi Tercih Etmiyor")

def hakkimda_bilgileri_goster():
    print("Worex Hakkında Bilgiler:")
    print("- Ad: Belirsiz")
    print("- Soyad: Belirsiz")
    print("- Meslek: Yazılım Geliştirici - Öğrenci")
    print("- Hobi: Python programlama, Gamer, spor")

if __name__ == "__main__":
    worex_menu()