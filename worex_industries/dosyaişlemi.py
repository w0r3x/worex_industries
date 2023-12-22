import time
import os

def worexdosya():
    dosya_klasoru = "worex_logg_klasörler/worex_oluşturulan_klasör"  # Dosyaların bulunacağı klasörü belirtin

    # Klasör var mı yok mu kontrol et, yoksa oluştur
    if not os.path.exists(dosya_klasoru):
        os.makedirs(dosya_klasoru)

    print("\033[91m===============================")
    print("|     Worex Industries        |")
    print("===============================\033[0m")
    print("╔─────────────────────────────╗")
    print("| 1- Dosya Oluştur            |")
    print("| 2- Dosya Oku                |")
    print("| 3- Dosya Yaz                |")
    print("| 4- Dosya Sil                |")
    print("| 5- Geri Dön                 |")
    print("╚─────────────────────────────╝")

    file_choice = input("Lütfen bir işlem seçin (1-5): ")

    if file_choice == "1":
        create_file(dosya_klasoru)
    elif file_choice == "2":
        read_file(dosya_klasoru)
    elif file_choice == "3":
        write_file(dosya_klasoru)
    elif file_choice == "4":
        delete_file(dosya_klasoru)
    elif file_choice == "5":
        pass
    else:
        print("Geçersiz seçim. Lütfen 1 ile 5 arasında bir sayı girin.")

def create_file(dosya_klasoru):
    file_name = input("Oluşturulacak TXT Dosyasının Adını Girin: ")
    full_path = os.path.join(dosya_klasoru, file_name)

    try:
        with open(full_path, 'w') as file:
            print(f"{file_name} dosyası oluşturuldu.")
    except Exception as e:
        print(f"Hata: {e}")

def read_file(dosya_klasoru):
    file_name = input("Okunacak dosyanın adını girin (örneğin, dosya_adı.txt): ")
    full_path = os.path.join(dosya_klasoru, file_name)

    try:
        with open(full_path, 'r') as file:
            content = file.read()
            print(f"{file_name} dosyası okundu. İçerik:\n{content}")
    except FileNotFoundError:
        print(f"{file_name} dosyası bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")

def write_file(dosya_klasoru):
    file_name = input("Oluşturulan dosyanın adını girin (örneğin, dosya_adı.txt): ")
    full_path = os.path.join(dosya_klasoru, file_name)
    content = input("Dosyaya yazılacak içeriği girin: ")

    try:
        with open(full_path, 'w') as file:
            file.write(content)
            print(f"{file_name} dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")

def delete_file(dosya_klasoru):
    file_name = input("Silinecek dosyanın adını girin (örneğin, dosya_adı.txt): ")
    full_path = os.path.join(dosya_klasoru, file_name)

    try:
        os.remove(full_path)
        print(f"{file_name} dosyası silindi.")
    except FileNotFoundError:
        print(f"{file_name} dosyası bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")
