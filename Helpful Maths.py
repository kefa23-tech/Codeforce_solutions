sums = list(input())
while "+" in sums:
    sums.remove("+")
sums = [int(i) for i in sums]
sums.sort()
if len(sums) > 1:
    sums =[str(i) for i in sums]
    print("+".join(sums))
else:
    print(sums[0])