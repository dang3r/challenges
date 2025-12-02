rngs = [rng.split("-") for rng in open("d2.in").read().split(",")]


def chunks(str, size):
    return [str[i : i + size] for i in range(0, len(str), size)]


invalid_p1 = 0
invalid_p2 = 0
for start, end in rngs:
    for i in range(int(start), int(end) + 1):
        v = str(i)
        if len(v) % 2 == 0 and v[: len(v) // 2] == v[len(v) // 2 :]:
            invalid_p1 += i
        for size in range(1, len(v) // 2 + 1):
            if len(v) % size == 0 and len(set(chunks(v, size))) == 1:
                invalid_p2 += i


print(invalid_p1)
print(invalid_p2)
