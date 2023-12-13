groups = open("d5.in").read().split("\n\n")

seeds = [int(val) for val in groups[0].split(" ")[1:]]
seed_to_vals = {seed: [seed] for seed in seeds}

for idx, group in enumerate(groups[1:]):
    lines = group.splitlines()
    ranges = []
    for line in lines[1:]:
        dst_start, src_start, length = [int(val) for val in line.split()]
        ranges.append((src_start, dst_start, length))
    for seed, elements in seed_to_vals.items():
        found = False
        for src_start, dst_start, length in ranges:
            if src_start <= elements[-1] < (src_start + length):
                delta = elements[-1] - src_start
                elements.append(dst_start + delta)
                break
        if not found:
            elements.append(elements[-1])

print(min(els[-1] for els in seed_to_vals.values()))
