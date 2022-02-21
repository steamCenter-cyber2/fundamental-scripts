# location 2:10
enc = "guvfvfngrfg"

ans = ""
for i in enc :
    if(ord(i) >=ord('a') and ord(i) <= ord('m')):
        ans += chr(ord(i)+13)
    else:
        ans += chr(ord(i)-13)

print(ans)