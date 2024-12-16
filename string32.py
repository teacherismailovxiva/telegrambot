# 32. Foydalanuvchidan Matnni 
# Har Bir So‘zning Oxirgi Harfini Chop Etish
# Salom dunyo
s1 = input('Matin kiriting: ')

s2 = s1.split()

for i in range(len(s2)):
    print(s2[i][-1])