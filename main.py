s1 = input("sfd: ")

katta_xarf = 0
kichik_xarf = 0
for i in range(len(s1)):
    if s1[i].isupper():
        katta_xarf += 1
    else:
        kichik_xarf += 1
print(katta_xarf)
print(kichik_xarf)