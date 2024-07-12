import sys
input = sys.stdin.readline

trie = {}

score = [0, 0, 0, 1, 1, 2, 3, 5, 11]
BOARD_SIZE = 4
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def insert_word_to_trie(trie, word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node[0] = 1

w = int(input())
for _ in range(w):
    word = input().strip()
    insert_word_to_trie(trie, word)

input()

def DFS(x, y, visited, node, current_word):
    if 0 in node:
        words.add(current_word)
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and not visited[nx][ny]:
            char = board[nx][ny]
            if char in node:
                DFS(nx, ny, visited, node[char], current_word + char)
    visited[x][y] = False

b = int(input())
for _ in range(b):
    board = [input().strip() for _ in range(4)]
    words = set()
    visited = [[False] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            char = board[x][y]
            if char in trie:
                DFS(x, y, visited, trie[char], char)
    
    max_score = sum(score[len(word)] for word in words)
    longest_word = ''
    
    if words:
        sorted_words = sorted(words)
        longest_word = max(sorted_words, key=len)
        
    print(max_score, longest_word, len(words))
    
    if _ != b - 1:
        input()
