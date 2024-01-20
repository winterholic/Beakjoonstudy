sum_multi = 0
sum_score = 0

score_dict = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

for i in range(20) :
    mystring = input()
    word = []
    for w in mystring.split() :
        word.append(w)
    if(word[2] == 'P') :
        continue
    sum_score += float(word[1])
    temp = float(word[1]) * score_dict[word[2]]
    sum_multi += temp

ans = sum_multi / sum_score

print(ans)