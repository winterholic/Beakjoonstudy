N, K = map(int, input().split())

triangle = [1]

for i in range(1, N + 2) :
    array = [1] * i
    triangle.append(array)

#print(triangle)

for i in range(3, N + 2) :
    for j in range(1, i - 1) :
        #print(i, j)
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

print((triangle[N + 1][K]) % 10007)