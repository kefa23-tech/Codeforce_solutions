# t = int(input())
# for _ in range(t):
#     n = input()
    
#     d = len(n)
#     ans = (d-1)*9
#     for i in range(1,10):
#         o = int(str(i)*d)
#         if o <= int(n):
#             ans+=1
#         else:
#             break
#     print(ans)
            

from math import abs

n = int(input())
boys = list(map(int,input().split()))
m = int(input())
girls = list(map(int,input().split()))
total = 0
for i in range(n):
    for j in range(m):
        if abs(boys[i] - girls[j]) == 1:
            total+=1
print(total)
print(000010**2)