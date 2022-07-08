val = 347991
i = 1

# How many steps from my square to the center?
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25 ---> ...
# The bottom right corner is the next square (1^2, 3^2, 5^2...)



while i ** 2 < val:
    i += 2
print(i, i // 2)
last_blocks = (i**2) - (i-2)**2
k  = last_blocks / 4
j = (val - (i-2)**2) % k
cp = (i // 2) - 1
print((i-2) // 2 + abs(j - cp))


vecs = [(1,0), (0,1), (-1,0), (0,-1)]
diag_vecs = vecs + [(1,1), (-1,-1), (1,-1), (-1, 1)]
v_i = 0
length = 1
pos = (0,0)
d = {(0,0): 1}
while True:
    for _ in range(2):
        for i in range(length):
            vec = vecs[v_i]
            pos = (pos[0] + vec[0], pos[1] + vec[1])
            value = 0
            for v in diag_vecs:
                value += d.get((pos[0] + v[0], pos[1] + v[1]), 0)
            d[pos] = value
            if value > val:
                input(value)
                break
        v_i = (v_i + 1) % 4
    length += 1
print(value)





