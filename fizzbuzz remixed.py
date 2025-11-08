
for _ in range(int(input())):
    n = int(input())
    total_blocks = (n + 1) // 15
    remainder = (n + 1) % 15
    answer = 3 * total_blocks + min(3, remainder)
    print(answer)
