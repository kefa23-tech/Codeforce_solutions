def greedy_grid_possible(n, m):
    # If either n or m is 1, it's impossible to construct such a grid
    if n == 1 or m == 1 or(n ==2 and m == 2):
        return "NO"
    return "YES"

# Input reading
t = int(input())  # Number of test cases
for _ in range(t):
    n, m = map(int, input().split())
    print(greedy_grid_possible(n, m))
