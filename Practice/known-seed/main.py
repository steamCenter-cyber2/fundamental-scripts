import random
import time 

msg = "flag{FAKE_FLAG}" # msg format = flag{msg_here}
random.seed(1337)

enc = bytearray()
for i in msg :
    enc.append(ord(i)^random.randint(1,255))

# with open("enc.txt",'wb') as f:
#     f.write(enc)

print(enc)

