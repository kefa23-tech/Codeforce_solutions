t = int(input())
for _ in range(t):
    n = int(input())
    beauty = list(map(int,input().split()))
    print(max(beauty)-min(beauty))