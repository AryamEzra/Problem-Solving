# from bisect import bisect_left
n = int(input())
pos = list(map(int, input().split()))
speed = list(map(int, input().split()))
min_pos = 0
max_pos = max(pos) - min(pos)
meet = sum(pos) / n

def helper(mid):
    global meet
    cur_min = float('inf')
    cur_max = float('-inf')
    time = 0
    for i in range(n):
        if pos[i] <= meet:
            time = pos[i] + (speed[i] * mid)
            cur_min = min(cur_min, time)   
        else:
            time = pos[i] - (speed[i] * mid)
            cur_max = max(cur_max, time)
    if cur_max <= cur_min:
        return True
    else:
        return False
ans = max_pos
while (max_pos - min_pos) > (1e-7):
    mid = (min_pos + max_pos) / 2
    if helper(mid): # true
        ans = mid
        max_pos = mid
    else:
        min_pos = mid
print(ans)