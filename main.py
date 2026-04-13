raw_data ="  AhMeT  yILMAZ ;  23 ;  1.78 ;  ahmetYILMAZ@GMAIL.Com   "
# veri temizliği
cleaned_data = raw_data.strip().lower() 
# parçalama işlemi
data_parts = cleaned_data.split(';')
name = data_parts[0].strip()
age = int(data_parts[1].strip())
height = float(data_parts[2].strip())
email = data_parts[3].strip()

#ismi düzenleme
name = name.replace("  "," ") #ismin başındaki ve sonundaki boşlukları kaldırır
name = name.title()  # isimdeki her kelimenin ilk harfini büyük yapar

#10 yıl sonra yaş
age += 10
age=float(age)

#boyu cm cinsine çevirme
height_cm=height*100

#email @ öncesi ilk 3 harf
email_index = email.find('@') # @ işaretinin konumunu bulur
email_username=email[:email_index][:3]


# Sonuçlar
print(f"User: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Height (cm): {height_cm}")
print(f"Email user code: {email_username}")
