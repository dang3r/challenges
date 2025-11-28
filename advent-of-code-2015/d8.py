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


def re_encoded_len(line) -> int:
    return len(line.replace("\\", "\\\\").replace('"', '\\"')) + 2


raw_total = sum(len(line) for line in lines)
str_total = sum(str_len(line) for line in lines)
enc_total = sum(re_encoded_len(line) for line in lines)
print(raw_total - str_total)

print(re_encoded_len(r'"\x27"'))

print(enc_total - raw_total)
