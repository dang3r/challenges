from collections import Counter, defaultdict

data = [int(val) for val in open("d11.in").read().strip().split()]
# data = [125, 17]

# part 1
for blink in range(25):
    new_data = []
    for element in data:
        if element == 0:
            new_data.append(1)
        elif len(str(element)) % 2 == 0:
            sel = str(element)
            idx = len(sel) // 2
            left = int(sel[:idx])
            right = int(sel[idx:])
            new_data.append(left)
            new_data.append(right)
        else:
            new_data.append(element * 2024)
    data = new_data

print(len(data))


# Part 2
data = [int(val) for val in open("d11.in").read().strip().split()]
d = Counter(data)
for blink in range(75):
    new_d = defaultdict(int)
    for element, count in d.items():
        if element == 0:
            new_d[1] += count
        elif len(str(element)) % 2 == 0:
            sel = str(element)
            idx = len(sel) // 2
            left = int(sel[:idx])
            right = int(sel[idx:])
            new_d[left] += count
            new_d[right] += count
        else:
            new_d[element * 2024] += count
    d = new_d

print(sum(new_d.values()))
