# location 2:9
import codecs 

user_input = input("please input test to rotate: ")
ans = codecs.encode(user_input,'rot_13')
print(ans)