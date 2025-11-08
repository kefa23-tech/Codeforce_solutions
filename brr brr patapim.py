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
    m = str(m)
    for i in codes:
        if str(i) not in m:
            m+=" " + str(i)
   
    
    print(m)
    