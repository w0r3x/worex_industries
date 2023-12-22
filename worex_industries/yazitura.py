import random  # random modülünü içe aktar

def worexyazitura():
    secenekler = ["Yazı", "Tura"]
    
    print("Yazı Tura Oyununa Hoş Geldin Dostum")
    oyuncu_secimi = input("Yazı mı, Tura mı? (y/t): ").lower()
    
    if oyuncu_secimi not in ["y", "t"]:
        print("\033[91mOlm mal mısın sen? 'y' veya 't' girsene\033[0m")
        return
    
    bilgisayar_secimi = random.choice(secenekler)
    
    print("Bilgisayarın Seçimi:", bilgisayar_secimi)
    
    if (oyuncu_secimi == "y" and bilgisayar_secimi == "Yazı") or (oyuncu_secimi == "t" and bilgisayar_secimi == "Tura"):
        print("\033[91m Tebrikler Güzel Tahmin :)\033[0m")
    else:
        print("\033[91m Üzgünüm dostum, bir dahaki sefere :)\033[0m")

