# s = list(input())


# i = 0
# while i < len(s)-1:
    
    
# print("".join(s))
s = input()
g = []
i=0
while i < len(s)-1:
    if s[i] == s[i+1] and s[i] == "/":
        g.append(i)
    i+=1

p = ""

for i in range(len(s)):
    if not i in g:
        p+=s[i]
    
if p[-1] == '/' and len(p) > 1:
    p = list(p)
    p.pop()
    p = "".join(p)
print(p)




    
    