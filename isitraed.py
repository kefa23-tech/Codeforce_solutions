t = int(input())
first,second = [],[]
for i in range(t):
    f,s = map(int,input().split())
    first.append(f)
    second.append(s)
if first == second:
    first.sort(reverse=True)
    if  first == second :
        print("maybe")
    else:
        print("unrated")
else:
    print("rated")

