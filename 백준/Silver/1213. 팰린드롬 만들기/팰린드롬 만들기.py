pelindrome = list(input())

alphabet = [0] * 26

cnt = 0

for pd in pelindrome :
    alphabet[ord(pd) - 65] += 1
    cnt += 1

ans = ""

i = 25
flag = 0

# print(alphabet)

while(True) :
    if(cnt <= 1) :
        break
    if(i == -1 and flag == 1) :
        i = 25
        flag = 0
    if(i == -1 and flag == 0) :
        break
    
    if(alphabet[i] >= 2) :
        while(alphabet[i] >= 2) : 
            alphabet[i] -= 2
            ans = chr(i + 65) + ans + chr(i + 65)
            cnt -= 2
        flag = 1

    i -= 1

if cnt == 1 :
    # print(cnt)
    index = 0
    for i in range(0, 26) :
        if(alphabet[i] == 1) :
            index = i
            break
    list_ans = list(ans)
    front_ans = list_ans[:len(list_ans) // 2]
    back_ans = list_ans[len(list_ans) // 2 :]
    ans = ''.join(front_ans) + chr(index + 65) + ''.join(back_ans)
    print(ans)

elif cnt == 0 :
    # print(cnt)
    print(ans)

else :
    # print(cnt)
    print("I'm Sorry Hansoo")

# str1 = "1234567"
# list_str1 = list(str1)
# f_str1 = list_str1[: len(list_str1) // 2]
# b_str1 = list_str1[len(list_str1) // 2 :]
# str2 = chr(1 + 65)
# str3 = "" 
# f_str1 = ''.join(f_str1)
# b_str1 = ''.join(b_str1)
# str3 = f_str1 + str2 + b_str1
# str4 = "aaa" + "ccc" + "dddd"
# str5 = str(list_str1)

# print(str1)
# print(list_str1)
# print(f_str1)
# print(b_str1)
# print(str2)
# print(str3)
# print(str4)
# print(str5)