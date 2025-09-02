def mex(arr):
    m = 1
    while m in arr:
        m+=1
    return m

t = int(input())
for _ in range(t):
    n = int(input())
    codes = []
    for i in range(n):
        r = list(map(int,input().split()))
        codes+=r
    
    
    m = mex(codes)
    password = [str(m)]
    for i in codes:
        if not str(i) in password:
            password.append(str(i))
    print(" ".join(password))
    