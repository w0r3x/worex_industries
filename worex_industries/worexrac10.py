import random
import time

def worexalemdar():
    while True:
        print("╔─────────────────────────╗")
        print("|     Worex - Alemdar     |")
        print("|         Rac10           |")
        print("|                         |")
        print("| 1- Polat Alemdar        |")
        print("| 2- Abdülhey Çoban       |")
        print("| 3- Memati Baş           |")
        print("| 4- Çıkış                |")
        print("╚─────────────────────────╝")

        secim = input("Lütfen bir seçenek numarası girin: ")

        if secim == "1":
            polat_alemdar_racon_sozleri()
        elif secim == "2":
            abdulhey_coban_racon_sozleri()
        elif secim == "3":
            memati_bas_racon_sozleri()
        elif secim == "4":
            print("Ana menüden çıkılıyor...")
            time.sleep(2)
            break
        else:
            print("Geçersiz bir seçenek girdiniz.")

def polat_alemdar_racon_sozleri():
    racon_sozleri = [
        "Ben sana son nefesin kadar yakın olacağım",
        "Benim yaşayan bir düşmanım yok!",
        "Ben soru sormam hesap sorarım.",
        "Beni tanırsınız, sakin olmamı istemezsiniz.",
        "Kimse benimle oyun oynamaz.",
        "Duygu güçsüzlerin sığınağıdır, onların mabedidir."
    ]

    random_soz = random.choice(racon_sozleri)

    print("Polat Alemdar'ın Racon Sözleri:")
    print("Sessiz Dedim:")
    print(random_soz)

def abdulhey_coban_racon_sozleri():
    racon_sozleri = [
        "Ölenin arkasından ağlama ki sen öldükten sonra arkandan ağlayan bırakma.",
        "Bizim bir adımız var, ezanla kondu selayla silinir biz iki günlük adamlara isim sildirmeyiz.",
        "Sen hiç mezar taşına delikanlı yazıldığını gördün mü?",
    ]

    random_soz = random.choice(racon_sozleri)

    print("Abdülhey Çoban'ın Racon Sözleri:")
    print("Sessiz Dedim:")
    print(random_soz)

def memati_bas_racon_sozleri():
    racon_sozleri = [
        "Zamanında o kadar paltosuz kezdik ki vücut eğik kaldı içimiz dik.",
        "Ben sana gülüm demem gülün ömrü az olur.",
        "Sen bende suç işlemekten korkan gözler görüyor musun?",
        "Senden yana bir sıkıntım olursa kafana sıkarım, rahat ol."
        "Geçmişini unutan geleceğini asla bulamaz."
    ]

    random_soz = random.choice(racon_sozleri)

    print("Memati Baş'ın Racon Sözleri:")
    print("Sessiz Dedim:")
    print(random_soz)

if __name__ == "__main__":
    worexalemdar()
