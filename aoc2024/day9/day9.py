with open("day9.txt", "r") as file:
    diskMap = file.read().strip()

isBlock = True
idNum = 0
disk =[]
# diskMap = "2333133121414131402"


for block in diskMap:
    c = (idNum // 2) if isBlock else "."
    for _ in range(int(block)):
        disk.append(str(c))
    idNum += 1
    isBlock = not isBlock

disk2 = disk.copy()

r = len(disk) - 1
for i in range(len(disk)):
    if disk[i] != ".":
        continue

    while disk[r] == ".":
        r -= 1

    if i >= r:
        break

    disk[i], disk[r] = disk[r], disk[i]
    r -= 1

def checksum(disk):
    total = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        total += int(disk[i]) * i
    return total

print(checksum(disk))



## PART 2

disk = disk2

r = len(disk) - 1

while r >= 0:
    if disk[r] == ".":
        r -= 1
    
    ## we are at a number
    n = disk[r]
    lenN = 0
    while disk[r] == n:
        lenN += 1
        r -= 1

    r += 1

    # now find a place to put this file if it exists
    for l in range(len(disk)):
        if l >= r:
            break

        if disk[l:l + lenN] == ["."] * (lenN):
            # we have space, swap
            disk[l: l + lenN], disk[r: r + lenN] = disk[r: r + lenN], disk[l: l + lenN]
            break
    
    r -= 1

print(checksum(disk))