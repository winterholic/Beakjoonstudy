N = int(input())

alpha_dict = {}

for char in range(ord('A'), ord('Z') + 1):
    alpha_dict[chr(char)] = 0

#print(alpha_dict)

alphabets = []
for i in range(N) :
    temp = input()
    alphabets.append(temp) # 알파벳 저장

for alphabet in alphabets :
    for i in range(len(alphabet)) :
        temp = 10 ** (len(alphabet) - 1 - i)
        alpha_dict[alphabet[i]] += temp

#print(alpha_dict)

numbers = []
for char in range(ord('A'), ord('Z') + 1) :
    if alpha_dict[chr(char)] > 0 :
        numbers.append(alpha_dict[chr(char)])

numbers = sorted(numbers, reverse = True)
sum = 0
current_num = 9

#print(numbers)

for i in range(len(numbers)) :
    sum += numbers[i] * current_num
    current_num -= 1

print(sum)