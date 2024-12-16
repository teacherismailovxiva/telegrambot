# 35. Foydalanuvchidan Matnni 
# Har Bir So‘zni Alifbo Tartibida Saralash

s1 = input('Matin kiriting: ')

s2 = s1.split()
s3 = sorted(s2, key=lambda x:x.lower())
print(s3)