import time
import worexhesap
import worexgame
import eokul
import iletişim
import sistembilgisi
import worexsayaç
import dosyaişlemi
import worexrac10

worex_tıkladığında = []

def main():
    print("                                              \033[91m===============================")
    print("                                              |       Worex Industries      |")
    print("                                              ===============================\033[0m")
    time.sleep(2)

    while True:
        worex_main_menu()

def worex_main_menu():
    print("╔─────────────────────────╗")
    print("|     Worex Industries    |")
    print("|                         |")
    print("| 1- Hesap Makinesi       |")
    print("| 2- Oyunlar              |")
    print("| 3- E-Okul Not Hesaplama |")
    print("| 4- Sistem Bilgisi       |")
    print("| 5- Dosya İşlemleri      |")
    print("| 6- Gün Hesaplama        |")
    print("| 7- İletişim             |")
    print("| 8- Rapor Oluştur        |")
    print("| 9- Rac10 (Tavsiyem Dışı)|")
    print("| 10- Çıkış               |")
    print("╚─────────────────────────╝")

    worexmeen = input("Lütfen bir işlem seçin (1-10): ")

    worex_tıkladığında.append(f"{get_operation_name(worexmeen)}'e giriş")

    if worexmeen == "1":
        worexhesap.worexh()
    elif worexmeen == "2":
        worexgame.gamemenu()
    elif worexmeen == "3":
        eokul.eokulnot()
    elif worexmeen == "4":
        sistembilgisi.sistem_bilgileri()
    elif worexmeen == "5":
        dosyaişlemi.worexdosya()
    elif worexmeen == "6":
        worexsayaç.gun_sayaci()
    elif worexmeen == "7":
        iletişim.iletisim_menu()
    elif worexmeen == "8":
        create_report()
    elif worexmeen == "9":
        worexrac10.worexalemdar()
    elif worexmeen == "10":
        print("Çıkış yapılıyor. İyi günler!")
        time.sleep(2)
        exit()
    else:
        print("Geçersiz seçim. Lütfen 1 ile 10 arasında bir sayı girin.")

    print("Worex'in Son Tıkladığı Seçimler:")
    for worex_geldi_ya_olm in worex_tıkladığında:
        print(worex_geldi_ya_olm)

    with open("worex_logg.txt", "a") as file:
        file.write("\n".join(worex_tıkladığında) + "\n")

def create_report():
    print("Rapor oluşturuluyor...")

def get_operation_name(choice):
    worex_bigi_ver_la = {
        "1": "Hesap Makinesi",
        "2": "Oyunlar",
        "3": "E-Okul Not Hesaplama",
        "4": "Sistem Bilgisi",
        "5": "Dosya İşlemleri",
        "6": "Gün Hesaplama",
        "7": "İletişim",
        "8": "Rapor Oluştur",
        "9": "Oto PC Kapatıcı",
        "10": "Çıkış",
    }
    return worex_bigi_ver_la.get(choice, "Bilinmeyen İşlem")

if __name__ == "__main__":
    main()
