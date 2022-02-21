# location 2:10
enc = "guvfvfngrfg"

# g -> a
ans =""
for i in enc:
    newNum = ord(i)-ord('a')
    newNum = (newNum +13)%26
    newChar = chr(newChar+ord('a'))
    ans +=newChar

print(ans)