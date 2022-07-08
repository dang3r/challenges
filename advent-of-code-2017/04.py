lines = [line.strip().split(' ') for line in open("04.in").readlines()]
valid_p1 = lambda x: len(x) == len(set(x))

count = 0
for line in lines:
    if valid_p1(line):
        count += 1
print(count)

# Forgot that sorted() returns a list. I expected it to return a sorted string and not a list.
count = 0
valid_p2 = lambda x: len(x) == len(set("".join(sorted(word)) for word in x))
for line in lines:
    if valid_p2(line):
        count += 1
print(count)
