i,j = map(int,input().split())
odds = [n for n in range(i) if n%2 != 0]

for r in range(i):
    if r in odds and odds.index(r) % 2 ==0 :
        for c in range(j):
            
            if c == j-1:
                print("#",end="")
            else:
                print(".",end="")
        print()
    elif r in odds and odds.index(r) % 2 !=0 :
        for c in range(j):
            if c == 0:
                print("#",end="")
            else:
                print(".",end="")
        print()
        
        
        
    else:    
        for c in range(j):
            print("#",end="")
        print()
    
        
        
       
    
        