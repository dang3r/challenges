from collections import defaultdict

lines = [line.strip() for line in open("07.in").readlines()]
dir_to_size = defaultdict(int)
path = []
idx = 0

while idx < len(lines):
    line = lines[idx]
    if line.startswith("$ cd"):
        next_dir = line.split(" ")[-1]
        if next_dir == "..":
            path.pop()
        elif next_dir == "/":
            path = ["/"]
        else:
            path.append(next_dir)
    elif line.startswith("$ ls"):
        while idx + 1 < len(lines) and not lines[idx + 1].startswith("$"):
            v1, v2 = lines[idx + 1].split(" ")
            if v1 != "dir":
                for i in range(len(path)):
                    normalized_path = "/".join(path[0 : i + 1])
                    dir_to_size[normalized_path] += int(v1)
            idx += 1
    idx += 1

total = sum([size for size in dir_to_size.values() if size <= 100000])
print(total)

disk_space_available = 70000000
disk_space_needed = 30000000
disk_space_used = dir_to_size["/"]
disk_space_to_free = disk_space_needed - (disk_space_available - disk_space_used)

answer = None
s = None
for path, size in dir_to_size.items():
    if size >= disk_space_to_free:
        if s is None or (size < s):
            s = size
            answer = path
print(s)
