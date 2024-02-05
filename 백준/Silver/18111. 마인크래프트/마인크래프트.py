N, M, B = map(int, input().split())

array = []

for i in range(N) :
    temp = list(map(int, input().split()))
    array.append(temp)

#print(array)

"""def heightcheck(array) :
    data = array[0][0]
    for i in range(N) :
        for j in range(M) :
            if(data != array[i][j]) :
                return False
    return True"""

min_height = 0
min_time = 1999999999

for k in range(257) :
    block = [0, 0]

    block[0] += B
    
    for i in range(N) :
        for j in range(M) :
            if(array[i][j] > k) :
                block[0] += array[i][j] - k
            else :
                block[1] += k - array[i][j]

    this_time = (block[0] - B) * 2 + block[1]
    
    if (block[1] - block[0] <= 0) and (min_time >= this_time):
        min_time = this_time
        min_height = k

print(min_time, min_height)