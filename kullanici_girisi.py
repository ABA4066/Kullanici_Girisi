from scipy.stats import gibrat

print("""
******************************

Kayıt Ol ve Sisteme Giriş Yap

******************************
""")

sys_ad = input("\nKullanıcı Adını Oluşturun\n")
sys_parola = input("\nParolayı Oluşturun\n")

print("\nKayıt Başarılı\nŞimdi Sisteme Giriş Yapınız\n")


giris_hakki=3

while True:

    adgir = input("\nKullanıcı Adı:\n")
    parogir = input("\nŞifre Gir\n")

    if(adgir == sys_ad and sys_parola == parogir):
        print("\nKullanıcı Adı ve Parola Doğru\n")
        print("\nSisteme Hoşgeldiniz...\n")
        break

    elif(adgir == sys_ad and sys_parola != parogir):
        print("\nKullanıcı Adı Doğru\nŞifre Yanlış\nErişim Reddidildi.")
        giris_hakki -= 1
        print("\n(Kalan Giriş Hakkınız {}'dir)\n".format(giris_hakki))

    elif(adgir != sys_ad and parogir == sys_parola):
        print("\nKullanıcı Adı Yanlış\nŞifre Doğru\nErişim Reddidildi.")
        giris_hakki -= 1
        print("\n(Kalan Giriş Hakkınız {}'dir)\n".format(giris_hakki))

    else:
        print("\nKullanıcı Adı ve Şifre Yanlış\nErişim Reddidildi.")
        giris_hakki -= 1
        print("\n(Kalan Giriş Hakkınız {}'dir)\n".format(giris_hakki))

    if giris_hakki == 0:
        print("Giriş Hakkınız Bitti...\n")
        print("Sistemden Çıkartılıyorsunuz...\n")
        break
