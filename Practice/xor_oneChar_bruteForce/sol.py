import base64

enc = "JC4jJTk2KisxHSsxHSMdNCcwOx0xNzInMB0xJyEwJzYdLycxMSMlJz8="
enc = base64.b64decode(enc)

for curr_key in range(256):
    curr_plain = ""
    for char in enc :
        curr_plain += chr(char^curr_key)
    print(curr_key,curr_plain)