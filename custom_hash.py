# location 3:9
msg = input("please input msg to calculate it's hash: ")

sumAll = 0
for i in msg :
    sumAll += ord(i)

print(sumAll%100)