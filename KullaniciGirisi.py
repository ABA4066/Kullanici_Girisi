print("""****************************************

Kayıt Ol ve Sisteme Giriş Yap

****************************************
""")

ad = input("\nKullanıcı Adını Oluşturun\n")
paro = input("\nParolayı Oluşturun\n")

print("\nKayıt Başarılı\nŞimdi Sisteme Giriş Yapınız\n")

adgir=input("\nKullanıcı Adı:\n")
parogir=input("\nŞifre Gir\n")


if(adgir == ad and paro == parogir):
    print("\nKullanıcı Adı ve Parola Doğru\n")
    print("\nSisteme Hoşgeldiniz...\n")
elif(adgir == ad and paro != parogir):
    print("\nKullanıcı Adı Doğru\nŞifre Yanlış\nErişim Reddidildi.")
elif(adgir != ad and parogir == paro):
    print("\nKullanıcı Adı Yanlış\nŞifre Doğru\nErişim Reddidildi.")
else:
    print("\nKullanıcı Adı ve Şifre Yanlış\nErişim Reddidildi.")
