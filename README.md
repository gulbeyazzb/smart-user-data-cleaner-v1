# smart-user-data-cleaner-v1

Veri Temizleme ve Dönüştürme Scripti

Bu Python scripti, ham (raw) kullanıcı verisini alır, temizler, düzenler ve anlamlı parçalara ayırarak işlenebilir hale getirir.

🚀 Amaç

Bu script aşağıdaki işlemleri gerçekleştirir:

String veriyi temizler (strip, lower)
Veriyi parçalara ayırır (split)
İsim formatını düzeltir
Yaşı hesaplar (10 yıl sonrası)
Boyu cm cinsine çevirir
Email kullanıcı adından kısa kod üretir

📥 Girdi (Input)
raw_data = "  AhMeT  yILMAZ ;  23 ;  1.78 ;  ahmetYILMAZ@GMAIL.Com   "

⚙️ Yapılan İşlemler

1. Veri Temizleme
cleaned_data = raw_data.strip().lower()

Baştaki ve sondaki boşluklar kaldırılır
Tüm karakterler küçük harfe çevrilir

3. Veriyi Parçalama
data_parts = cleaned_data.split(';')

Veri şu alanlara ayrılır:
İsim
Yaş
Boy
Email

3. Veri Tipi Dönüşümleri
name = data_parts[0].strip()
age = int(data_parts[1].strip())
height = float(data_parts[2].strip())
email = data_parts[3].strip()

5. İsim Formatlama
name = name.replace("  ", " ")
name = name.title()

Fazla boşluklar temizlenir
Her kelimenin ilk harfi büyük yapılır

📌 Örnek:
ahmet  yilmaz → Ahmet Yilmaz

5. Yaş Hesaplama
age += 10
age = float(age)

Kullanıcının 10 yıl sonraki yaşı hesaplanır
Float tipine çevrilir

7. Boy Dönüştürme
height_cm = height * 100

Boy metre → santimetreye çevrilir

9. Email Kodu Üretme
email_index = email.find('@')
email_username = email[:email_index][:3]

@ öncesiden ilk 3 karakter seçilir

📌 Örnek:
ahmetyilmaz@gmail.com → ahm

📤 Çıktı (Output)

<img width="176" height="72" alt="Screenshot 2026-04-13 at 20 35 55" src="https://github.com/user-attachments/assets/3a062499-f307-40a8-98bb-ed9d44a3e77f" />
