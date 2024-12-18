EMPTY = "."

data = [int(val) for val in open("d9.in").read().strip()]


def create_blocks():
    a = []
    for i in range(len(data)):
        if i % 2 == 0:
            idx = i // 2
            a.extend([idx] * data[i])
        else:
            a.extend([EMPTY] * data[i])
    return a


a = create_blocks()
i = 0
j = len(a) - 1
while i < j and 0 <= i < len(a) and 0 <= j < len(a):
    while 0 <= i < len(a) and a[i] != EMPTY:
        i += 1
    while 0 <= j < len(a) and a[j] == EMPTY:
        j -= 1
    if i < j:
        a[i] = a[j]
        a[j] = EMPTY
print(sum(idx * val for idx, val in enumerate(a) if val != EMPTY))


empty = []
full = []
a = []
for i in range(len(data)):
    if i % 2 == 0:
        idx = i // 2
        full.append((len(a), len(a) + data[i] - 1))
        a.extend([idx] * data[i])
    else:
        empty.append((len(a), len(a) + data[i] - 1))
        a.extend([EMPTY] * data[i])

for f_start, f_end in full[::-1]:
    f_sz = f_end - f_start + 1
    for e_idx in range(len(empty)):
        e_start, e_end = empty[e_idx]
        e_sz = e_end - e_start + 1
        if e_sz >= f_sz and e_end < f_start:
            for i in range(f_sz):
                a[e_start + i] = a[f_start + i]
                a[f_start + i] = EMPTY

            # Tweak list of empty intervals
            if e_start + f_sz <= e_end:
                empty = empty[:e_idx] + [(e_start + f_sz, e_end)] + empty[e_idx + 1 :]
            else:
                empty = empty[:e_idx] + empty[e_idx + 1 :]
            break

print(sum(idx * val for idx, val in enumerate(a) if val != EMPTY))
