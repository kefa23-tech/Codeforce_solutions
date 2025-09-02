l1 = list(map(str,input().split()))
l2 = list(map(str,input().split()))
l3 = list(map(str,input().split()))
lines = [l1,l2,l3]
v = "aeiou"
vs = 0
sy = 0
for line in lines:
    for word in line:
        for ch in range(len(word)-1):
            if word[ch] in v and (not word[ch+1]  in v):
                vs+=1 
                sy+=1
if vs == sy:
    print("Yes")
else:
    print("No")
            
    