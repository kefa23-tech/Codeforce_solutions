t = int(input())
for _ in range(t):
    n,p = map(int,input().split())
    arr = list(map(int,input().split()))
    l = arr[0]
    r = arr[-1]
    result = min(abs(p-l),abs(p-r))+ (r-l)
    print(result)