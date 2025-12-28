from collections import defaultdict

with open("day11.txt", "r") as file:
    stones = file.read().strip().split(" ")

stones = [int(s) for s in stones]
sd = defaultdict(int)
for s in stones:
    sd[s] += 1

total = 0

for b in range(75):
    nextS = defaultdict(int)
    for s, n in sd.items():
        if s == 0:
            nextS[1] += n
        elif len(str(s)) % 2 == 0:
            ss = str(s)
            m = len(ss) // 2
            nextS[int(ss[:m])] += n
            nextS[int(ss[m:])] += n
        else:
            nextS[s * 2024] += n
    sd = nextS

print(sum(sd.values()))