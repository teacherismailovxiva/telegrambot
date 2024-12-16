#26. Foydalanuvchidan Matndan Raqamlarni Ajratib Olish

s1 = input("String kiriting = ")

number = []
for i in range(len(s1)):
    if s1[i].isdigit():
        number.append(s1[i])
print(number)