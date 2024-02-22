t = int(input())
for _ in range(t):
    n = int(input())
    a = input()

    dic = {0:1}
    summ = 0
    ans = 0
    for i in range(n):
        summ += int(a[i])
        l = summ - 1 - i
        
        if l not in dic:
            dic[l] = 0
        dic[l] += 1

        ans += (dic[l] - 1)
        
    print(ans)
    