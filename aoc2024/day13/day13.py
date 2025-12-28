import math
from functools import cache

with open("day13.txt", "r") as file:
    file = file.readlines()

machines = []
curr = []
for line in file:
    if line == '\n':
        machines.append(curr)
        curr = []
        continue
    
    _, x ,y = line.strip().replace("=", "+").split("+")
    x = x.partition(",")[0]
    curr.append((int(x), int(y)))

machines.append(curr)

@cache
def moves(targetx, targety, currx, curry, ax, ay, bx, by, apush, bpush):
    if targetx == currx and targety == curry:
        return 3 * apush + bpush
    
    if currx > targetx or curry > targety or apush > 100 or bpush > 100:
        return float('inf')

    pressa = moves(targetx, targety, currx + ax, curry + ay, ax, ay, bx, by, apush + 1, bpush)
    pressb = moves(targetx, targety, currx + bx, curry + by, ax, ay, bx, by, apush, bpush + 1)

    return min(pressa, pressb)


total = 0

for (ax, ay), (bx, by), (targetx, targety) in machines:
    tokens = moves(targetx, targety, 0, 0, ax, ay, bx, by, 0 ,0)
    if math.isinf(tokens):
        tokens = 0
    total += tokens

print(total)