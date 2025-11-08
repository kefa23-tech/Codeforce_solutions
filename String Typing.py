n = int(input())
s = input()
ss = list(set(s))
ss.sort()
ss = "".join(ss)
print(ss)

if  ss == s:
    print(n)
else:
   n-= s.count(ss)
   print(n)
