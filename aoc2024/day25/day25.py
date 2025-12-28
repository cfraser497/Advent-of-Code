with open("day25.txt", "r") as file:
    ss = file.read().strip().split("\n\n")

    schematics = []
    for s in ss:
        schematics.append(s.split("\n"))

# determine keys and locks and convert to col format
keys, locks = [], []
for s in schematics:
    if s[0][0] == "#":
        lock = []
        for col in range(len(s[0])):
            for row in range(len(s)):
                if s[row + 1][col] == ".":
                    lock.append(row)
                    break

        locks.append(tuple(lock))
    else:
        key = []
        for col in range(len(s[0])):
            for row in range(len(s) - 1, -1, -1):
                if s[row - 1][col] == ".":
                    key.append(len(s) - 1 - row)
                    break
        
        keys.append(tuple(key))

print(keys)
print(locks)

lockSize = len(schematics[0])
pairs = 0

for lock in locks:
    for key in keys:
        fits = True
        for i in range(len(key)):
            if lock[i] + key[i] > lockSize - 2:
                fits = False

        if fits:
            pairs += 1

print(pairs)

        