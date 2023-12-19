groups = open("d5.in").read().split("\n\n")
original_positions = [int(val) for val in groups[0].split(" ")[1:]]

ranges = []
for idx, group in enumerate(groups[1:]):
    lines = group.splitlines()
    group = []
    for line in lines[1:]:
        dst_start, src_start, length = [int(val) for val in line.split()]
        group.append((dst_start, src_start, length))
    ranges.append(group)

# Part  1
positions = original_positions.copy()
for idx, group in enumerate(ranges):
    new_positions = []
    for position in positions:
        found = False
        for dst_start, src_start, length in group:
            if src_start <= position < (src_start + length):
                delta = position - src_start
                new_positions.append(dst_start + delta)
                found = True
                break
        if not found:
            new_positions.append(position)
    positions = new_positions

print("MIN", min(positions))

# Part 2
positions = [
    (original_positions[i], original_positions[i] + original_positions[i + 1] - 1)
    for i in range(0, len(original_positions), 2)
]
print(positions)
for idx, group in enumerate(ranges):
    new_positions = []
    for position in positions:
        new_ones = []
        new_ranges = []
        print("Starting range", position)
        for dst_start, src_start, length in group:
            # Detect if the two line segments intersect
            if (position[0] >= src_start and position[0] < (src_start + length)) or (
                src_start >= position[0] and (src_start < (position[1]))
            ):
                new_pos = max(position[0], src_start), min(
                    position[1], src_start + length - 1
                )
                new_ranges.append(new_pos)

                delta = new_pos[0] - src_start + dst_start
                delta2 = new_pos[1] - src_start + dst_start
                new_pos = (delta, delta2)
                new_ones.append(new_pos)

        print("new ranges,", new_ranges)
        # If a range does not intersect any lines, it remains the same
        if not new_ranges:
            print("NONE")
            new_positions.append(position)
            continue

        # Identify all gaps in the original range with the untranslated new ranges
        # if a gap exists, just add it back
        new_ranges = sorted(new_ranges)
        gaps = []
        if new_ranges[0][0] != position[0]:
            gaps.append((position[0], new_ranges[0][0] - 1))

        for i in range(0, len(new_ranges) - 1):
            if new_ranges[i][1] != new_ranges[i + 1][0] - 1:
                gaps.append((new_ranges[i][1] + 1, new_ranges[i + 1][0] - 1))

        if new_ranges[-1][1] != position[1]:
            gaps.append((new_ranges[-1][1] + 1, position[1]))
        print("gaps", gaps)

        new_positions.extend(new_ones)
        new_positions.extend(gaps)

    print(positions)
    print(new_positions)
    positions = new_positions

print("MIN", min(positions))
