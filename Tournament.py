t = int(input())

for _ in range(t):
    n,j,k = map(int,input().split())
    a = list(map(int,input().split()))
    print("yes" if k > 1 or a[j-1] == max(a) else "no")