import sys
input = sys.stdin.readline

N = int(input())

times = list(map(int, input().split()))

sum_times = 0

real_sum = 0

for i in range(N) :
    min_value = min(times)
    min_index = times.index(min_value)
    times[min_index] = 1001 + i
    temp_sum = sum_times
    sum_times += min_value
    #print("data" , min_value, sum_times, temp_sum)
    real_sum += sum_times

print(real_sum)