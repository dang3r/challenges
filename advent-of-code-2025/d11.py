import functools

lines = open("d11.in").read().splitlines()
d = dict()
for line in lines:
    tokens = line.split()
    src = tokens[0][:-1]
    d[src] = tokens[1:]


@functools.lru_cache
def p1(src: str) -> int:
    if src == "out":
        return 1

    total = 0
    for dst in d[src]:
        total += p1(dst)
    return total

total = p1("you")
print(total)



@functools.lru_cache
def p2(src: str, target: str, disallow: str) -> int:
    if src == target:
        return 1
    if src == disallow or not src in d:
        return 0

    total = 0
    for dst in d[src]:
        total += p2(dst, target, disallow)
    return total

svr_dac = p2("svr", "dac", "fft")
dac_fft = p2("dac", "fft", "out")
fft_out = p2("fft", "out", "")

svr_fft = p2("svr", "fft", "dac")
fft_dac = p2("fft", "dac", "out")
dac_out= p2("dac", "out", "")

total = svr_dac*dac_fft*fft_out
total += svr_fft*fft_dac*dac_out
print(total)

