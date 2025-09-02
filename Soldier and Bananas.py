k,n,w = map(int,input().split())
lst = [i*k for i in range(1,w+1)]
total = sum(lst)

print(total - n if n < total else 0)