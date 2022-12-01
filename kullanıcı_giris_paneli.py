# pratiklik için fonksiyonlarımı tanımlıyorum

def kullanıcı_adı_al():
    data["kullanıcı_adı"] = str(input("Kullanıcı adınızı girinz: "))

def sifre_al():
    data["sifre"] = str(input("Sifrenizi giriniz: "))

def sifre_onay_al():
    data["sifre_onay"] = str(input("Sifrenizi onaylayınız: "))


# dictionary'mi olutuşturdum
data = {}



print("Hoşgeldiniz..")

# eğer kayıtlı kullanıcı bulunmazsa kaydolma adımları izlenecek

# if bool(data["kullanıcı_adı"]) == False:
print(" --------------- Kayıtlı hesap bulunamamıştır. Hesap oluşturmanız gerekmektedir. ----------------")
print(" --------------- Lütfen adımları sırasıyla izleyiniz ----------------")

kullanıcı_adı_al()

# ilk girilen şifre ile dogrulama  şifresi aynı olana kadar tekrar dogrulama şifresi istenecek



while True:

    sifre_al()
    sifre_onay_al()

    if str(data["sifre"]) == str(data["sifre_onay"]):
        print("Şifre başarıyla onaylamıştır !!!")
        break

    else:
        print("Girdiğiniz şifre, ilk şifrenizle uyuşmuyor lütfen ilk şifrenin aynınsı giriniz.")

        
        


print("----------------- Kayıt tamamlandı ---------------------")
print("------------- KULLANICI ADINIZ: " + str(data["kullanıcı_adı"]) + " ---------")
print("------------- ŞİFRENİZ: " + str(data["sifre"]) + " ---------------------")

# -------------- Kayıt tamamlandı ------------------

# -------------- Oturum Açma -----------------------

print("Oturum Açınız..")

while True:

    giris_kullanıcı_adı = str(input("Kullanıcı Adı: "))
    giris_sifre = str(input("Şifre: "))

    #print("(test) dict deki kullanıcı adı: " + str(data["kullanıcı_adı"]))
    #print("(test) dict deki şifre: " + str(data["sifre"]))

# birinci koşul false dönüyor, ikinci koşul true
# birinci koşulda dict'den aldığım değer ['a'] olarak gözüküyor ama benim girdim sadece a
# birinci koşulu true döndürebilirsem eğer program tam anlamıyla çalışacak.

    if str(data["kullanıcı_adı"]) == str(giris_kullanıcı_adı) and str(data["sifre"]) == str(giris_sifre):
        print("Başarıyla giriş yapıldı !!!")
        break
    else:
        print("Hatalı giriş. Lütfen tekrar giriniz...")