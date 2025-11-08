import bisect

n = int(input())
prices = list(map(int,input().split()))
prices.sort()
days = int(input())


for _ in range(days):
    m = int(input())
    count = bisect.bisect_right(prices,m)
    print(count)
    

