import random

def worexbilir():
    bilmeceler = [
        {"soru": "İki kapaklı, içinde dünya saklı, Açıp bakınca gökyüzü karşı, Ne bu?", "cevap": "Kitap"},
        {"soru": "Beyazdır, sarıdır, yazın gelir kışı karartır, Bir kuş var ağaçta, Yuvası sarı, kanadı karadır, Ne bu?", "cevap": "Mektup"},
        {"soru": "İki tel bir tele ne demiş? Kavuşamayız demiş.", "cevap": "Çorap"},
        {"soru": "İki gider, bir gelir, Birleşirse harika bir enerji kaynağı olur, Ne bu?", "cevap": "Güneş ve Ay"},
        {"soru": "Beyazdır kağıt, kara yazı yazar, Evet der, hayır der, Bir de kocaman kafası var, Ne bu?", "cevap": "Kalem"}
    ]

    random.shuffle(bilmeceler)

    for bilmece in bilmeceler:
        print("Soru:", bilmece["soru"])
        tahmin = input("Cevabınızı yazın: ").capitalize()

        if tahmin == bilmece["cevap"]:
            print("Tebrikler! Doğru cevap.")
        else:
            print(f"Maalesef yanlış. Doğru cevap: {bilmece['cevap']}")
