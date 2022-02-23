import base64

plain = "dummy_msg"

enc = bytearray()

key = 'Dummy_key' # key length = 1 

for i in plain :
    enc.append(key^ord(i))

# output in enc.txt
print(base64.b64encode(enc))