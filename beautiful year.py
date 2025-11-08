t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    ones = [i for i,ch in enumerate(s) if ch == "1"]
    if not ones:
        print(0)
        continue
    protected = 0
    last = -k
    for i in ones:
        if i-last < k:
            continue
        protected+=1
        last = i
    print(protected)    
