import sys
input = sys.stdin.readline

answers = []

def calculation(num1, num2, char) :
    if (char == 0) :
        return (num1 + num2)
    elif (char == 1) :
        return (num1 - num2)
    elif (char == 2) :
        return (num1 * num2)
    elif (char == 3) :
        return int((num1 / num2))

ans = []

def DFS() :
    if len(ans) == len(result) :
        temp_ans = 0
        i = 0
        for number in ans :
            if (i == 0) :
                temp_ans = calculation(numbers[0], numbers[1], result[number])
            else :
                temp_ans = calculation(temp_ans, numbers[i + 1], result[number])
            i += 1
        answers.append(temp_ans)
        return
    
    for i in range(0, len(result)) :
        if i in ans :
            continue
        ans.append(i)
        DFS()
        ans.pop()
        
n = int(input())  # 개수 입력

# 숫자 입력 받아 리스트에 저장
numbers = list(map(int, input().split()))

# 연산자의 개수는 항상 4개로 고정되어 있다고 가정
temp_oper = list(map(int, input().split()))

result = [idx for idx, count in enumerate(temp_oper) for _ in range(count)]

DFS()

print(max(answers))
print(min(answers))