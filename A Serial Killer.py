today,tomor = map(str,input().split())
n = int(input())
print(today,tomor)
for i in range(n):
    
    t , tm = map(str,input().split())
    if today == t:
        today = tm
    else:
        tomor = tm
    print(today,tomor)
    
        