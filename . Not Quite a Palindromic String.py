t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    c0 = s.count('0')
    c1 = n - c0

    min_good = abs(c0 - c1) // 2
    max_good = (c0 // 2) + (c1 // 2)
    if min_good <= k <= max_good and ((n//2 - k) % 2 == c0 % 2):
        print("YES")
    else:
        print("NO")
