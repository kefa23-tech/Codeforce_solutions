t = int(input())

for _ in range(t):
    
    n = int(input())
    s = input()
    found = False
    for ch in set(s):
        n_ch = s.count(ch)
        if n_ch >= 3:
            found = True
            break
    if not found:
        for ch in set(s):
            n_ch = s.count(ch)
            if n_ch == 2 :
                first = s.find(ch)
                last = s.rfind(ch)
                if first != 0 or last != n - 1: 
                    found = True
                    break
    
    print("yes" if found else "no")
            


