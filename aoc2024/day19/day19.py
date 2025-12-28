with open("day19.txt", "r") as file:
    towels, designs = file.read().strip().split("\n\n")

    towels = list(map(lambda t: t.strip(), towels.split(",")))
    designs = list(map(lambda d: d.strip(), designs.split("\n")))

# Originally did this with functools cache but decided to give dp a shot
dp = {}
def backtrack(d):
    if d in dp:
        return dp[d]

    if d == "":
        return 1

    ways = 0
    for t in towels:
        start = d[:len(t)]
        if start == t:
            ways += backtrack(d[len(t):])

    dp[d] = ways
    return ways


poss = 0
ways = 0

for d in designs:
    w = backtrack(d)
    poss += 1 if w > 0 else 0
    ways += w

print(poss)
print(ways)