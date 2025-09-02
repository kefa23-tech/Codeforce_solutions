t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    if min(s) == max(s):
        print("NO")
    elif s < s[::-1] :
        print("YES")
    elif k >= 1:
        print("YES")
    else:
        print("NO")

