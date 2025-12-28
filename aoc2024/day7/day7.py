from itertools import product

with open("day7.txt", "r") as file:
    D = file.read().strip().split('\n')

# Target is always E[i][0]
Es = []
for line in D:
    l = line.split(" ")
    
    # Remove colon
    l[0] = l[0][:-1]
    l = [int(n) for n in l]

    Es.append(l)


total = 0

for target, *nums in Es:
    ops = list(product(["*", "+", "||"], repeat=len(nums) - 1))

    for opList in ops:
        curr = nums[0]
        nextIdx = 1
        for op in opList:
            if curr > target:
                break

            if op == "+":
                curr += nums[nextIdx]
            if op == "*":
                curr *= nums[nextIdx]
            if op == "||":
                n = nums[nextIdx]
                for _ in range(len(str(n))):
                    curr *= 10
                curr += n

            nextIdx += 1
        if curr == target:
            total += target
            break

print(total)

