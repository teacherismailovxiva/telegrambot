from random import randint

list = []
for i in range(3):
        x = randint(2, 6)
        y = randint(2, 8)
        list.append(({'savol':f"{x}+{y}", "a":x+y, 'b':x+y-1, 'c':x+y-3}))

for x in list:
    print(f"Salom: {x['savol']} \nA){x['a']} \nB){x['b']} \nC){x['c']}")