import platform
import os
import psutil

def sistem_bilgileri():
    bilgisayar_adı = platform.node()
    işletim_sistemi = platform.system()
    işletim_sistemi_sürümü = platform.version()
    işletim_sistemi_mimarisi = platform.architecture()
    işlemci = platform.processor()
    
    bellek = psutil.virtual_memory().total // (1024 ** 3)  # GB cinsinden toplam bellek
    kullanılan_bellek = psutil.virtual_memory().used // (1024 ** 3)  # GB cinsinden kullanılan bellek
    boşta_bellek = psutil.virtual_memory().available // (1024 ** 3)  # GB cinsinden boşta olan bellek

    disk_bilgileri = psutil.disk_usage('/')
    toplam_disk = disk_bilgileri.total // (1024 ** 3)  # GB cinsinden toplam disk kapasitesi
    kullanılan_disk = disk_bilgileri.used // (1024 ** 3)  # GB cinsinden kullanılan disk alanı
    boşta_disk = disk_bilgileri.free // (1024 ** 3)  # GB cinsinden boşta olan disk alanı

    kullanıcı_adı = os.getlogin() if os.name == 'posix' else os.getenv('USERNAME')

    print("Sistem Bilgileri:")
    print(f"- Bilgisayar Adı: {bilgisayar_adı}")
    print(f"- İşletim Sistemi: {işletim_sistemi}")
    print(f"- İşletim Sistemi Sürümü: {işletim_sistemi_sürümü}")
    print(f"- İşletim Sistemi Mimarisi: {işletim_sistemi_mimarisi}")
    print(f"- İşlemci: {işlemci}")
    print(f"- Toplam Bellek: {bellek} GB")
    print(f"- Kullanılan Bellek: {kullanılan_bellek} GB")
    print(f"- Boşta Bellek: {boşta_bellek} GB")
    print(f"- Toplam Disk Alanı: {toplam_disk} GB")
    print(f"- Kullanılan Disk Alanı: {kullanılan_disk} GB")
    print(f"- Boşta Disk Alanı: {boşta_disk} GB")
    print(f"- Kullanıcı Adı: {kullanıcı_adı}")