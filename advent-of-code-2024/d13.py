import re

lines = open("d13.in").read().splitlines()


def groups():
    for i in range(0, len(lines), 4):
        a = re.search(r"X\+(\d+), Y\+(\d+)", lines[i]).groups()
        b = re.search(r"X\+(\d+), Y\+(\d+)", lines[i + 1]).groups()
        c = re.search("X=(\d+), Y=(\d+)", lines[i + 2]).groups()

        a = tuple([int(val) for val in a])
        b = tuple([int(val) for val in b])
        c = tuple([int(val) for val in c])
        yield a, b, c


def part1():
    gs = list(groups())
    total = 0

    for a, b, c in gs:
        lowest = float("+inf")
        for a_num in range(100):
            for b_num in range(100):
                cost = a_num * 3 + b_num
                res = (
                    a[0] * a_num + b[0] * b_num,
                    a[1] * a_num + b[1] * b_num,
                )
                if res == c:
                    lowest = min(lowest, cost)

        if lowest != float("+inf"):
            total += lowest

    return total


def part2():
    gs = list(groups())
    total = 0

    for a, b, c in gs:
        # a*x_0 + b*x_1 = C
        # a*y_0 + b*y_1 = D
        # Solve for b and then a
        x = [a[0], b[0]]
        y = [a[1], b[1]]
        c = list(c)
        c[0] += 10000000000000
        c[1] += 10000000000000
        C = c[0]
        D = c[1]

        print(x, y, C, D)

        b_num = (D * x[0] - C * y[0]) / (-1 * x[1] * y[0] + y[1] * x[0])
        a_num = (C - b_num * x[1]) / x[0]
        if b_num >= 0 and a_num >= 0 and int(b_num) == b_num and int(a_num) == a_num:
            total += 3 * int(a_num) + int(b_num)

    return total


print(part1())
print(part2())
