t = int(input())
for _ in range(t):
    n = int(input())
    tooth = list(map(int,input().split()))
    unrepeated = set(tooth)
    if len(unrepeated) == len(tooth) :
        print("No")  
    else:
        print("Yes")
          
