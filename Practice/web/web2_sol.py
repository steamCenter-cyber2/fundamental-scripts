import hashlib


def check(s):
    return s[:2] == "0e" and s[2:].isdigit()


salt = "f789bbc328a3d1a3"
i = 0
while True:
    curr_pass = salt + str(i)
    # do the hash
    curr_result = hashlib.md5(curr_pass.encode()).hexdigest()
    if check(curr_result):
        print(i)
        break

    if i % 1000000 == 0:
        print(i)
    i += 1
