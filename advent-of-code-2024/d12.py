data = open("d12.testin").read().splitlines()


def in_region(x, y, label):
    return (0 <= x < len(data[0]) and 0 <= y < len(data)) and data[y][x] == label


def find_region(x, y):
    label = data[y][x]
    area = 0
    perimeter = 0
    nodes = set([(x, y)])
    seen = set()

    while nodes:
        # The same node in a region can be added by multiple others. Dedupe.
        n_x, n_y = nodes.pop()
        if (n_x, n_y) in seen:
            continue

        seen.add((n_x, n_y))
        area += 1

        candidates = [
            (n_x + 1, n_y),
            (n_x - 1, n_y),
            (n_x, n_y - 1),
            (n_x, n_y + 1),
        ]
        for c_x, c_y in candidates:
            if not in_region(c_x, c_y, label):
                perimeter += 1
            elif data[c_y][c_x] == label and (c_x, c_y) not in seen:
                nodes.add((c_x, c_y))

    return area, perimeter, seen


def sides(coords) -> int:
    seen = set()
    sides = 0
    for x, y in coords:
        label = data[y][x]
        candidates = [
            (x + 1, y),
            (x - 1, y),
            (x, y - 1),
            (x, y + 1),
        ]
        for c_x, c_y in candidates:
            if not in_region(c_x, c_y, label):
                v_x, v_y = c_x - x, c_y - y
                if (x, y, v_x, v_y) in seen:
                    continue
                seen.add((x, y, v_x, v_y))
                if v_x:
                    # check all boxes on y axis
                    n_y = y - 1
                    while in_region(x, n_y, label) and not in_region(
                        x + v_x, n_y + v_y, label
                    ):
                        seen.add((x, n_y, v_x, v_y))
                        n_y -= 1
                    n_y = y + 1
                    while in_region(x, n_y, label) and not in_region(
                        x + v_x, n_y + v_y, label
                    ):
                        seen.add((x, n_y, v_x, v_y))
                        n_y += 1
                elif v_y:
                    # check all boxes on x axis
                    n_x = x - 1
                    while in_region(n_x, y, label) and not in_region(
                        n_x + v_x, y + v_y, label
                    ):
                        seen.add((n_x, y, v_x, v_y))
                        n_x -= 1
                    n_x = x + 1
                    while in_region(n_x, y, label) and not in_region(
                        n_x + v_x, y + v_y, label
                    ):
                        seen.add((n_x, y, v_x, v_y))
                        n_x += 1
                sides += 1
    return sides


groups = []
seen = set()
for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) not in seen:
            area, perimeter, coords = find_region(x, y)
            groups.append((area, perimeter, coords))
            seen = seen.union(coords)


# Part 1
total_price = sum(a * p for a, p, c in groups)
print(total_price)

# Part 2
total_price = sum(a * sides(c) for a, p, c in groups)
print(total_price)
