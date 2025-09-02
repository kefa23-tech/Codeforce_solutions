t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    ls = [i for i in range(n)]
    ls.pop()
    ls = [ str(i+1) for i in ls]
    ls.append(str(x))
    print(" ".join(ls))
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())    
    for i in range(x):
        print(i,end=" ")
    for i in range(x+1,n):
        print(i,end=" ") 
    if x < n:
        print(x,end=" ")
    print()