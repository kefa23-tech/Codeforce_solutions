n,m = map(int,input().split())
lights = 0
for _ in range(n):
    lis = list(map(int,input().split()))
    for j in range(m):
        if lis[j*2] ==  1 or lis[j*2 +1] == 1:
            lights +=1
print(lights)
            
