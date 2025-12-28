from collections import Counter

with open('day1.txt', 'r') as file:
    numbers = file.read().split()

numbers = [int(num) for num in numbers]

list1 = []
list2 = []

for i, number in enumerate(numbers):
    if i % 2 == 0:
        list1.append(number)
    else:
        list2.append(number)

list1 = sorted(list1)
list2 = sorted(list2)

diff = 0
for n1, n2 in zip(list1, list2):
    diff += abs(n1 - n2)

print(diff)

## PART 2

count = Counter(list2)

similarity = 0

for n1 in list1:
    if n1 in count:
        similarity += n1 * count[n1]

print(similarity)


