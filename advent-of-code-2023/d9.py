lines = open("d9.in").read().splitlines()
total = 0
first_total = 0

for line in lines:
    digits = [int(item) for item in line.split()]
    diffs = []
    diffs.append(digits)
    diffs.append([digits[i] - digits[i - 1] for i in range(1, len(digits))])
    while any([diff != 0 for diff in diffs[-1]]):
        diffs.append(
            [diffs[-1][i] - diffs[-1][i - 1] for i in range(1, len(diffs[-1]))]
        )

    diffs = diffs[::-1]
    for i in range(1, len(diffs)):
        diffs[i].insert(0, diffs[i][0] - diffs[i - 1][0])
        diffs[i].append(diffs[i - 1][-1] + diffs[i][-1])
    new_token = diffs[-1][-1]

    # EOL
    #    print(new_token)
    total += new_token

    # SOL
    #    print(diffs[-1][0])
    first_total += diffs[-1][0]

print(total)
print(first_total)
