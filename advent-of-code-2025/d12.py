import dataclasses
from collections import Counter

lines = open("d12.in").read().split("\n\n")
shape_strs = lines[:-1]
areas = lines[-1].splitlines()

@dataclasses.dataclass
class Shape:
    idx: int
    area: list[list[str]]

    def size(self):
        return Counter("".join(self.area))["#"]

shapes = dict()
for sh in shape_strs:
    lines = sh.splitlines()
    s = Shape(
        idx=int(lines[0][0]), 
        area=lines[1:],
    )
    shapes[s.idx] = s


def p1():
    yes = no = maybe 0
    for area in areas:
        width = int(area[:2])
        length = int(area[3:5])
        nums = {int(idx):int(p) for idx, p in enumerate(area.split(" ")[1:])}
        rect_area = width*length
        shape_area = sum(total*shapes[idx].size() for idx, total in nums.items())
        if rect_area < shape_area:
            no += 1
        elif (width // 3) * (length//3) >= sum(nums.values()):
            yes += 1
        else:
            maybe +=1
    print(yes, no, maybe)

p1()
