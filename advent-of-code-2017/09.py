g = open("09.in").read().strip()

depth = 0
i = 0
total = 0
gbg_total = 0
while i < len(g):
    char = g[i]
    if char == "{":
        depth += 1
        i += 1
    elif char == "<":
        i += 1
        while g[i] != ">":
            if g[i] == "!":
                i += 2
            else:
                gbg_total += 1
                i += 1
        i += 1
    elif char == "}":
        total += depth
        depth -= 1
        i += 1
    else:
        i += 1
print(total)
print(gbg_total)