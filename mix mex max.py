def mex(arr):
    arr = set(arr)
    
    m = 0
    while m in arr:
        m+=1
    return m
    


    
t = int(input())

for _ in range(t):

    n = int(input())
    nums = list(map(int,input().split()))
    while -1 in nums:
        nums.remove(-1)
   
    s = set(nums)
    
   
    if len(s) == 0  or (len(s)==1 and not 0 in s):
        print("YES")
    else:
        print("NO")
    
            
   