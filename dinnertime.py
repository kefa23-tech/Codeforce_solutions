t = int(input())
for _ in range(t):
    n,m,p,q = map(int,input().split())
    print("NO"  if m - q == p else "YES") 