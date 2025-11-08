t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    cakes = list(map(int,input().split()))
    max_cakes = 0
    cakes.sort(reverse = True)
    
    for cake in cakes:
        if m > 0 :
            max_cakes+=cake*m
            m-=1
    print(max_cakes)