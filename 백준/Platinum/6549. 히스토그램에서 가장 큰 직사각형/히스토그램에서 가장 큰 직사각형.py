import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    out_lines = []
    
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        if n == 0:
            break

        arr = [int(next(it)) for _ in range(n)]
        
        size = 1
        while size < n:
            size *= 2
        tree = [-1] * (2 * size)

        for i in range(n):
            tree[size + i] = i

        for i in range(size - 1, 0, -1):
            left = tree[2 * i]
            right = tree[2 * i + 1]
            if left == -1:
                tree[i] = right
            elif right == -1:
                tree[i] = left
            else:
                tree[i] = left if arr[left] <= arr[right] else right

        def query_iter(l, r):
            l += size
            r += size
            res = -1
            while l <= r:
                if l & 1:
                    if res == -1 or (tree[l] != -1 and arr[tree[l]] < arr[res]):
                        res = tree[l]
                    l += 1
                if not (r & 1):
                    if res == -1 or (tree[r] != -1 and arr[tree[r]] < arr[res]):
                        res = tree[r]
                    r -= 1
                l //= 2
                r //= 2
            return res

        max_area = 0
        stack = [(0, n - 1)]
        while stack:
            start, end = stack.pop()
            if start > end:
                continue
            m = query_iter(start, end) 
            area = arr[m] * (end - start + 1)
            if area > max_area:
                max_area = area
            stack.append((start, m - 1))
            stack.append((m + 1, end))
        
        out_lines.append(str(max_area))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()
