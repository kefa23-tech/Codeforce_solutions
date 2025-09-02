t = int(input())
for _ in range(t):
    s = input().strip()
    # last non-zero position
    p = len(s) - 1
    while s[p] == '0':
        p -= 1
    zeros_before = s[:p].count('0')
    kept = zeros_before + 1
    print(len(s) - kept)

