import random
import time


with open("enc.txt", "rb") as f:
    enc = f.read()


base_time = 1646005200  # 2:40 AM
for i in range(10000):
    curr_seed = base_time + i
    random.seed(curr_seed)

    plain = ""
    for e in enc:
        plain += chr(e ^ random.randint(1, 255))

    if "flag{" in plain:
        print(plain)
