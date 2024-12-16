# 25. Foydalanuvchidan 
# Matnda Kichik va Katta Harflar Sonini Hisoblash
#PythonDasturlashTili -> 3 ta katta 17

s1 = input("String kiriting: ")

katta_harf = 0
kichik_harf = 0
for i in range(len(s1)):
    if s1[i].isupper():
        katta_harf += 1
    else:
        kichik_harf += 1
print("Katta harflar soni= ", katta_harf)
print("Kichik harflar sono= ", kichik_harf)