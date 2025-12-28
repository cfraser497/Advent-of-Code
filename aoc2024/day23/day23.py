from collections import defaultdict

with open("day23.txt", "r") as file:
    connections = file.read().strip().split("\n")
    connections = list(map(lambda c: c.split("-"), connections))

networkMap = defaultdict(list)
for i, j in connections:
    networkMap[i].append(j)
    networkMap[j].append(i)

sets = set()

for c1, c2s in networkMap.items():
    for i, c2 in enumerate(c2s):
        for j in range(i + 1, len(c2s)):
            if c2s[j] in networkMap[c2]:
                sets.add(tuple(sorted([c1, c2, c2s[j]])))

totalTs = 0
for s in sets:
    for c in s:
        if c[0] == "t":
            totalTs += 1
            break

print(totalTs)

## Part 2

def backtrack(cs, biggestSet):
    if cs == []:
        return biggestSet
    
    canAdd = True
    for c in biggestSet:
        if cs[0] not in networkMap[c]:
            canAdd = False
    
    if not canAdd:
        return backtrack(cs[1:], biggestSet).copy()
    
    biggestSet.add(cs[0])
    set1 = backtrack(cs[1:], biggestSet).copy()
    biggestSet.remove(cs[0])
    set2 = backtrack(cs[1:], biggestSet).copy()

    return set1 if len(set1) >= len(set2) else set2


biggest = set()
for c, cs in networkMap.items():
     b = backtrack(cs, set([c]))
     if len(biggest) < len(b):
         biggest = b

# Arrange alphabetically
password = ",".join(sorted(biggest))
print(password)