from lib import *

lines = open("d9.in").read().splitlines()
#lines = open("d9.testin").read().splitlines()
points = [tuple(map(int, line.split(","))) for line in lines]

points_to_svg(points)

area = lambda pt1, pt2: (abs(pt1[0]-pt2[0])+1)*(abs(pt1[1]-pt2[1])+1)
biggest = float("-inf")

for i, pt1 in enumerate(points):
    for pt2 in points[i+1:]:
        biggest = max(biggest, area(pt1, pt2))
print(biggest)


# draw border
y_to_xr = dict()
for (x1,y1), (x2, y2) in zip(points, points[1:] + points[:1]):
    mnx, mxx = sorted([x1,x2])
    mny, mxy = sorted([y1,y2]) 
    if y1 == y2:
        if y_to_xr.get(y1):
            mn,mx = y_to_xr[y1] 
            y_to_xr[y1] = (min(mn,mnx), max(mx,mxx))
        else:
            y_to_xr[y1] = (mnx, mxx)
    else:
        for y in range(mny, mxy+1):
            if y_to_xr.get(y):
                mn,mx = y_to_xr[y] 
                y_to_xr[y] = (min(mn,x1), max(mx,x1))
            else:
                y_to_xr[y] = (x1, x1)

def gucci(pt1,pt2):
    x1,y1 = pt1
    x2,y2 = pt2
    mnx, mxx = sorted([x1,x2])
    mny, mxy = sorted([y1,y2]) 

    for y in range(mny, mxy+1):
        mn, mx = y_to_xr[y]
        if not all(mn <= x <= mx for x in [x1,x2]):
            return False
    return True

biggest = float("-inf")
for i, pt1 in enumerate(points):
    for pt2 in points[i+1:]:
        if gucci(pt1,pt2):
            a = area(pt1,pt2)
            biggest = max(a, biggest)
print(biggest)



