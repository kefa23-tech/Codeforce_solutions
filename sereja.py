n,d = map(int,input().split())
a = list(map(int,input().split()))
m = int(input())
if n < m:
    print(((n-m)*d) + sum(a))
else:
    print(sum(a[n-m:]))
    
