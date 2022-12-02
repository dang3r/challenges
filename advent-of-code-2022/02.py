lines = [line.strip().split() for line in open("2.in").readlines()]
moves = [(ord(l[0]) - ord("A"), ord(l[1]) - ord("X")) for l in lines]
win = lambda opp, my: my == (opp + 1) % 3
draw = lambda opp, my: my == opp
score = lambda mv: mv + 1

total = 0
for mv0, mv1 in moves:
    total += score(mv1)
    if draw(mv0, mv1):
        total += 3
    elif win(mv0, mv1):
        total += 6
print(total)

total = 0
for opp_move, outcome in lines:
    opp_move = ord(opp_move) - ord("A")
    if outcome == "X":
        my_move = (opp_move - 1) % 3
    elif outcome == "Y":
        total += 3
        my_move = opp_move
    elif outcome == "Z":
        total += 6
        my_move = (opp_move + 1) % 3
    total += score(my_move)
print(total)
