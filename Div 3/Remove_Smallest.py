def check_array():
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        sorted_flag = True
        for j in range (0, n-1):
            if (abs(a[j]-a[j+1]) <= 1):
                continue
            else:
                print("No")
                sorted_flag = False
                break
        if sorted_flag:
            print("Yes")
        t -= 1
check_array()