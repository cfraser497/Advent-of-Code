from collections import defaultdict

with open("day22.txt", "r") as file:
    secrets = file.read().strip().split("\n")
    secrets = [int(s) for s in secrets]

def mix(s, n):
    s ^= n
    return s

def prune(s):
    s %= 16777216
    return s

def next(s):
    n = s * 64
    s = mix(s, n)
    s = prune(s)

    n = s // 32
    s = mix(s, n)
    s = prune(s)

    n = s * 2048
    s = mix(s, n)
    s = prune(s)

    return s



NUM_GENERATIONS = 2000

total = 0
sequenceTotals = defaultdict(int)

for s in secrets:
    prices = [int(str(s)[-1])]
    changes = []
    added = set()

    for i in range(NUM_GENERATIONS):
        s = next(s)
        price = int(str(s)[-1])
        prices.append(price)
        changes.append(prices[i + 1] - prices[i])

        if i >= 3 and (changes[i - 3], changes[i - 2], changes[i - 1], changes[i]) not in added:
            added.add((changes[i - 3], changes[i - 2], changes[i - 1], changes[i]))
            sequenceTotals[(changes[i - 3], changes[i - 2], changes[i - 1], changes[i])] += prices[i + 1]

    total += s

print(total)
maxS = max(sequenceTotals.items(), key=lambda s: s[1])
print(maxS)
