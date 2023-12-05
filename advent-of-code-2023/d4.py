from collections import defaultdict

lines = open("d4.in").read().splitlines()


# part 1
points = 0
for idx, line in enumerate(lines):
    sets = line.split(":")[1].split("|")
    assert len(sets) == 2
    good_cards = set(sets[0].split())
    my_cards = set(sets[1].split())
    intersect = good_cards & my_cards
    if len(intersect) >= 1:
        points += 2 ** (len(intersect) - 1)
print(points)

# part 2
card_idx_to_count = defaultdict(int)
for idx, line in enumerate(lines):
    card_idx_to_count[idx] += 1
    sets = line.split(":")[1].split("|")
    good_cards = set(sets[0].split())
    my_cards = set(sets[1].split())
    matching_numbers = len(good_cards & my_cards)

    # Add new cards
    for j in range(idx + 1, idx + 1 + matching_numbers):
        card_idx_to_count[j] += 1 * card_idx_to_count[idx]


print(sum(card_idx_to_count.values()))
