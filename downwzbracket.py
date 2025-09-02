t = int(input())
for _ in range(t):
    s = input()
    balance = 0
    ok = False
    for c in s[1:-1]:
        if c == "(":
            balance+=1
        else:
            balance-=1
        if balance < 0 :
            ok = True
    print("Yes" if ok or balance != 0 else"NO")
        
    