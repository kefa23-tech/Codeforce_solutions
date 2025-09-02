t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    pattern = "10"
    p = ""
    for _ in range(n):
        p+=pattern
    print(p[:n])
