n = int(input())
lst = list(map(int,input().split()))
start = 0
end = n
d = {}
while start < end :
    l = min(lst[start:end])
    r = max(lst[start:end])
    if r - l <= 1 :
        if r -l not in d:
            d[r-l] = (start,end)
    start+=1
print(d)
m = d[min(d.keys())]
s = m[0]
e = m[1]
print(s,e)