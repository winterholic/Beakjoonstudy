from itertools import combinations

N, K = map(int, input().split())

words_bitmask = []

for _ in range(N):
    word = input().strip()
    bitmask = 0
    for char in word:
        bitmask |= (1 << (ord(char) - ord('a'))) 
    words_bitmask.append(bitmask)

# for bitmask in words_bitmask:
#     print(bin(bitmask))

if K < 5:
    print(0)
    exit()

essential_bitmask = 0
for char in "antic":
    essential_bitmask |= (1 << (ord(char) - ord('a')))

remaining_letters = [i for i in range(26) if not (essential_bitmask & (1 << i))]

max_count = 0

for comb in combinations(remaining_letters, K - 5):
    selected_bitmask = essential_bitmask
    for letter in comb:
        selected_bitmask |= (1 << letter)

    count = 0
    for word_bitmask in words_bitmask:
        if word_bitmask & selected_bitmask == word_bitmask:
            count += 1

    max_count = max(max_count, count)

print(max_count)