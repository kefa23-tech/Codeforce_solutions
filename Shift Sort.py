for _ in range(int(input())):
    n = int(input())
    s = input()
    s = list(s)
    left = 0
    right = n-1
    operations = 0
    while left < right:
        if int(s[left]) > int(s[right]):
            s[left],s[right]= s[right],s[left]
            operations+=1
        elif s[left] == "1" and s[right] == "1":
            right-=1
        else:
            left+=1
            
    print(operations)
        
