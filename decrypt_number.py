# location 2:7
nums = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]

ans = ""
for i in nums :
    curr_chr = chr(ord('a')+i-1)
    ans += curr_chr
    # ans = ans+curr_chr
print(ans)