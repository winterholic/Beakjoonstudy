mystring = ['@']
temp = input()
mystring += list(temp)
mystring.append('@')

len_str = len(temp)
cnt = 0
i = 1

#print(mystring)
#print(len_str)

cnt = 0
i = 1
while i <= len_str :
    if(mystring[i] == 'c') :
        if(mystring[i + 1] == '-' or mystring[i + 1] == '=') :
            #print(mystring[i], mystring[i + 1], cnt)
            cnt += 1
            i += 2
            continue
        else :
            #print(mystring[i], cnt)
            cnt += 1
            i += 1
            continue
    if(mystring[i] == 'd') :
        if(mystring[i + 1] == '-') :
            #print(mystring[i], mystring[i + 1], cnt)
            cnt += 1
            i += 2
            continue
        else :
            #print(mystring[i])
            cnt += 1
            i += 1
            continue
    if(mystring[i] == 'z') :
        if(mystring[i + 1] == '=') :
            if(mystring[i - 1] == 'd') :
                #print(mystring[i - 1], mystring[i], mystring[i + 1], cnt)
                i += 2
                continue
            else :
                #print(mystring[i], mystring[i + 1], cnt)
                cnt += 1
                i += 2
                continue
        else :
            #print(mystring[i], cnt)
            cnt += 1
            i += 1
            continue
    if(mystring[i] == 'l') :
        if(mystring[i + 1] == 'j') :
            #print(mystring[i], mystring[i + 1], cnt)
            cnt += 1
            i += 2
            continue
        else :
            #print(mystring[i], cnt)
            cnt += 1
            i += 1
            continue
    if(mystring[i] == 'n') :
        if(mystring[i + 1] == 'j') :
            #print(mystring[i], mystring[i + 1], cnt)
            cnt += 1
            i += 2
            continue
        else :
            #print(mystring[i], cnt)
            cnt += 1
            i += 1
            continue
    if(mystring[i] == 's') :
        if(mystring[i + 1] == '=') :
            #print(mystring[i], mystring[i + 1], cnt)
            cnt += 1
            i += 2
            continue
        else :
            #print(mystring[i], cnt)
            cnt += 1
            i += 1
            continue
    else :
        #print("나머지", mystring[i], cnt)
        cnt += 1
        i += 1
        continue

#print(i)
print(cnt)