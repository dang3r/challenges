def correct_order(update: list) -> list:
    new = [-1 for _ in update]
    for it1 in update:
        idx = 0
        for it2 in update:
            if it2 in d[it1]:
                idx += 1
        new[idx] = it1
    assert not any(-1 == it for it in new)
    print(new)
    return new
        
text = open("d5.in").read()

rules, updates = text.split("\n\n")

from collections import defaultdict
d = defaultdict(set)
rules = [rule.split("|") for rule in rules.splitlines()]
for before, after in rules:
    d[before].add(after)

#assert len(rules) == (len(d)*(len(d) - 1) / 2), (len(rules), (len(d)))


updates = [update.split(",") for update in updates.splitlines()]


total = 0
p2_total = 0
for update in updates:
    seen = set()
    good = True
    for current in update:
        if any(num in d[current] for num in seen):
            good = False
            correct = correct_order(update)
            p2_total += int(correct[len(correct) // 2])

            break
        seen.add(current)
    if good:
        total += int(update[len(update) // 2])
print(total)


print(p2_total)