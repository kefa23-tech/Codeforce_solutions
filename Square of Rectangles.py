def can_form_square(rects):
    # Normalize so that for each rectangle (longer side first)
    rects = [(max(a, b), min(a, b)) for a, b in rects]
    S = max(max(a, b) for a, b in rects)  # candidate square side

    # Case A: All three must align to S in one dimension
    count_S = [a == S or b == S for a, b in rects].count(True)
    if count_S == 3:
        # collect the "other sides" where one dimension == S
        others = []
        for a, b in rects:
            if a == S:
                others.append(b)
            elif b == S:
                others.append(a)
        if sum(others) == S:
            return True

    # Case B: One rectangle takes part, others fill leftover
    for i in range(3):
        a, b = rects[i]
        if a == S:  # rectangle spans full side
            rem = S - b
            others = rects[:i] + rects[i+1:]
            # both must have one side = rem, other sides add up to S
            if all(rem in r for r in others):
                widths = [r[0] if r[1] == rem else r[1] for r in others]
                if sum(widths) == S:
                    return True
    return False


# Driver
t = int(input())
for _ in range(t):
    vals = list(map(int, input().split()))
    rects = [(vals[0], vals[1]), (vals[2], vals[3]), (vals[4], vals[5])]
    print("YES" if can_form_square(rects) else "NO")
