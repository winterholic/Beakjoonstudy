N = int(input())

cnt = 0

for i in range(N) :
    word = input()
    my_queue = []
    flag = 1
    my_queue.append(word[0])
    for i in range(1, len(word)) :
        if(word[i - 1] != word[i]) :
            if(word[i] in my_queue) :
                flag = 0
                break
        my_queue.append(word[i])
    if (flag == 1) :
        cnt += 1

print(cnt)