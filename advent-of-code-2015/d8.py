lines = open("d8.in", "r").read().splitlines()


def str_len(line) -> int:
    i = 0
    count = 0
    while i < len(line):
        if line[i : i + 2] == r"\\" or line[i : i + 2] == r"\"":
            i += 2
        elif line[i : i + 2] == r"\x":
            i += 4
        else:
            i += 1
        count += 1

    return count - 2


code_total = sum(len(line) for line in lines)
str_total = sum(str_len(line) for line in lines)
print(code_total - str_total)
