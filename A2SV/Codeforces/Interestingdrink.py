from bisect import bisect_right
n = int(input())
prices = list(map(int, input().split()))
days = int(input())
prices.sort()
for _ in range(days):
    n = int(input())
    idx = bisect_right(prices, n)
    print(idx)