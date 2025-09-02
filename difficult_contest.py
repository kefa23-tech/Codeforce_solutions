
t = int(input())
for _ in range(t):
    s = input()
    s = [ord(ch) for ch in s]
    s.sort(reverse=True)
    s = [chr(n) for n in s]
    print("".join(s))
