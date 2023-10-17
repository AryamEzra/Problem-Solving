t = int(input())
a = list(map(int, input().split()))
o,e = 0,0
for i in range(t):
    if a[i] % 2 == 0:
        e += 1
    else:
        o += 1
if e != 0 and o != 0:
    a.sort()
    print(*a)
else:
    print(*a)