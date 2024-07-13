from collections import deque

N, K = map(int, input().split())
N_str = str(N)
M = len(N_str)
    
queue = deque([(N_str, K)])
visited = set([(N_str, K)])
max_num = -1

while queue:
    curr, new = queue.popleft()
        
    if new == 0:
        max_num = max(max_num, int(curr))
        continue
        
    for i in range(M):
        for j in range(i + 1, M):
            if i == 0 and curr[j] == '0':
                continue

            numbers = list(curr)
            numbers[i], numbers[j] = numbers[j], numbers[i]
            new_number = ''.join(numbers)
                
            if (new_number, new - 1) not in visited:
                visited.add((new_number, new - 1))
                queue.append((new_number, new - 1))
    
if max_num == -1:
    print(-1)
else:
    print(max_num)