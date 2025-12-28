from collections import defaultdict

def getData():
    rules = []
    updates = []
    with open("day5.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                break

            rules.append(line)

        for line in file:
            updates.append(line.strip())

    return rules, updates



rules, updates = getData()

# int -> set(int)
# Maps from pages to all pages that must come before it
pageRules = defaultdict(set)

for rule in rules:
    before, after = rule.split('|')
    pageRules[after].add(before)

validUpdates = []
invalidUpdates = []

for update in updates:
    # Check if the update is valid
    # An update is invalid if a page exists in the pageRules map after the current page
    pages = update.split(",")

    valid = True
    for i, page in enumerate(pages):
        for j in range(i + 1, len(pages)):
            if pages[j] in pageRules[page]:
                valid = False

    if valid:
        validUpdates.append(pages)
    else:
        invalidUpdates.append(pages)


validTotal = 0

for update in validUpdates:
    m = len(update) // 2

    validTotal += int(update[m])

print(f"VALID TOTAL: {validTotal}") 


invalidTotal = 0

for update in invalidUpdates:
    print("UPDATE")
    print(update)

    for page in update:
        print(f"PAGE: {page}")
        print(pageRules[page])


print(f"INVALID TOTAL: {invalidTotal}")

# print(pageRules)
# print(rules)
# print(updates)