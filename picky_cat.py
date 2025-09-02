from statistics import median
from math import ceil
t = int(input())

    
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    my_arr = [abs(i) for i in arr]
    if median(arr) == arr[0]:
        print("Yes")
    elif len(arr) == 1:
        print("Yes")
    else:
        if my_arr[0] == max(my_arr):
            print("NO")
        else:
            print("Yes")
    
    # m = arr[0]
    # n_arr = arr[:]
    # found = False
    # for i in range(n):
    #     n_arr.sort()
    #     if len(arr)%2 == 2:
    #         mdn = len(arr)//2 - 1
    #         if arr(mdn) == m:
    #             print("Yes")
    #             found = True
    #             break
    #     else:
    #         if median(n_arr) == m:
    #             print("Yes")
    #             found = True
    #             break
    #         else:
    #             n_arr[-1]*=-1
    # if not found:
    #     print("NO")

            