L, C = map(int, input().split())

# 입력 받기
input_str = input()

# 공백을 기준으로 나누어 리스트로 저장
values = input_str.split()

values = sorted(values)

"""# 리스트의 각 값에 접근
for value in values:
    print(value)"""

def DFS(pw, index) :
    if(len(pw) == L) :
        flag = 0
        Vowel = 0
        consonant = 0
        for i in range(len(pw)) :
            if(pw[i] == 'a' or pw[i] == 'i' or pw[i] == 'e' or pw[i] == 'o' or pw[i] == 'u') :
                Vowel += 1
            else :
                consonant += 1
        if(Vowel >= 1 and consonant >= 2) :
            flag = 1
        if (flag == 1) :
            for char in pw :
                print(char, end = "")
            print()
    
    for i in range(index + 1, C) :
        if(values[i] in pw) :
            continue
        
        pw.append(values[i])
        DFS(pw, i)
        pw.pop()

pw = []
DFS(pw, -1)