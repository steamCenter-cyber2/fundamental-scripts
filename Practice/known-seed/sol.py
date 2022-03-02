import random

random.seed(1337)

with open("enc.txt",'rb') as f :
    enc = f.read()


keys = list()
for i in range(25):
    keys.append(random.randint(1,255))
print(keys)
# for i in enc:
# for i in range(len(enc)):
#     print(chr(enc[i]^keys[i]),end="")
