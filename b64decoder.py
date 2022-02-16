# location 2:5
import base64

curr_msg = input("please input base64 string to decode it : ")
result = base64.b64decode(curr_msg)

print(f"the decoded output is : {result}")
