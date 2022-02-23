# python3 my_hash_cracker.py hash list.txt

import sys 
import hashlib

hash = sys.argv[1]
wordlist = sys.argv[2]

with open(wordlist,'r') as f :
    words = f.readlines()

flag = True  

for word in words:
    word = word.strip()
    curr_hash = hashlib.md5(word.encode()).hexdigest()
    if curr_hash == hash :
        print(f"found it .. the word is : {word}")
        flag = False


if flag :
    print("no password found... ")