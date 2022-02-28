
with open('enc_img.png','rb')as f:
    img = f.read()


key = "superkey" # key length = 8


enc_img= bytearray()
for i in range(len(img)):
    enc_img.append(img[i]^ord(key[i%8]))

with open("img.png",'wb') as f :
    f.write(enc_img)


