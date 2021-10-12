names = ['Nic','Noc','Nac','Nec']

def crowd(names):
    if len(names) > 3:
        print("crowded")

crowd(names)
names.pop(1)
names.pop(2)
crowd(names)