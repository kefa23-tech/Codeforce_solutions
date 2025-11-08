from math import sqrt
def isprime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0 :
            return False
    return True
t = int(input())
for _ in range(t):
    x,k= map(str,input().split())
    if x == 1:
        print("YES" if k == 2 else "NO")
    elif k == 1:
        print("YES" if isprime(x) else "NO") 
    else:
        print("NO")     
    # x*=int(k)
    # print("YES" if isprime(int(x)) else "NO")
  
