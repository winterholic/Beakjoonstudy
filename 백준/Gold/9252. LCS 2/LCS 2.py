A = input()
B = input()

#print(A, B)

dp = [[0] * (len(B) + 1) for _ in range((len(A) + 1))]

#print(dp)

for i in range(1, len(A) + 1) :
    for j in range(1, len(B) + 1) :
        if(A[i - 1] == B[j - 1]) :
            dp[i][j] = dp[i - 1][j - 1] + 1
        else :
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

#print(dp)
print(dp[len(A)][len(B)])

# for d in dp :
#     print(*d)

A = list(A)
B = list(B)

i = len(A)
j = len(B)

LCSstr = ""

while i > 0 and j > 0 :
    if dp[i][j] == dp[i][j - 1] :
        j -= 1
    elif dp[i][j] == dp[i - 1][j] :
        i -= 1
    else :
        LCSstr = B[j - 1] + LCSstr
        i -= 1
        j -= 1

print(LCSstr)