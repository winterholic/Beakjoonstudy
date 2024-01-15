import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]

visited = [False] * 26
count = 1  # 시작점의 알파벳도 카운트해야 하므로 초기값을 1로 설정

def is_valid(x, y):
    return 0 <= x < R and 0 <= y < C

def DFS(x, y, depth):
    global count
    count = max(count, depth)

    visited[ord(board[x][y]) - 65] = True
    direction = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]

    for direct in direction:
        px = direct[0]
        py = direct[1]
        if is_valid(px, py) and not visited[ord(board[px][py]) - 65]:
            DFS(px, py, depth + 1)

            # 백트래킹
            visited[ord(board[px][py]) - 65] = False

DFS(0, 0, 1)
print(count)