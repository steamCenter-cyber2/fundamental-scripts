with open('tux.png','rb')as f:
    img = f.read()


key = "Dummy_key" # key length = 8 


enc_img= bytearray()
for i in range(len(img)):
    enc_img.append(img[i]^ord(key[i%8]))


with open("enc_img.png",'wb') as f :
    f.write(enc_img)
