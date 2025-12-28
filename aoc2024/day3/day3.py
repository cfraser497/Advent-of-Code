import re

text = ""
with open ("day3.txt", "r") as file:
    text = file.read()

muls = re.findall(r"mul\((\d+),\s*(\d+)\)", text)

total = 0

for x, y in muls:
    total += int(x) * int(y)

print(total)

## PART 2

total = 0

dos = re.split(r"do\(\)", text)

muls = []
for i, phrase in enumerate(dos):
    beforeDonts = re.search(r"^(.*?)don't\(\)", phrase)
    if beforeDonts:
        phrase = beforeDonts.group(1)
    muls += re.findall(r"mul\((\d+),\s*(\d+)\)", phrase)
        
for x, y in muls:
    total += int(x) * int(y)

print(total)