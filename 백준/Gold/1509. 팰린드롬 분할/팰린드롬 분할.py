def minCut(s):
    n = len(s)
    cut = [0] * n
    is_palindrome = [[False] * n for _ in range(n)]

    for i in range(n):
        min_cut = i  # 최대로 가능한 cut 수
        for j in range(i + 1):
            if s[i] == s[j] and (i - j < 2 or is_palindrome[j + 1][i - 1]):
                is_palindrome[j][i] = True
                min_cut = 0 if j == 0 else min(min_cut, cut[j - 1] + 1)
        cut[i] = min_cut

    return cut[-1]

s = input()
print(minCut(s) + 1)