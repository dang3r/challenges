data = open("1.in", "r").read()
elves = data.split("\n\n")
elf_totals = [sum(map(int, elf.split("\n"))) for elf in elves]

print(max(elf_totals))
print(sum(sorted(elf_totals)[-3:]))
