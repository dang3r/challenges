lines = open("13.in").read().splitlines()


def right_order(s1, s2):
    # print("Comparing", s1, s2)
    for v1, v2 in zip(s1, s2):
        correct = None
        if type(v1) == type(v2) == int and v1 < v2:
            correct = True
        if type(v1) == type(v2) == int and v1 > v2:
            correct = False
        elif type(v1) == list and type(v2) == int:
            correct = right_order(v1, [v2])
        elif type(v1) == int and type(v2) == list:
            correct = right_order([v1], v2)
        elif type(v1) == type(v2) == list:
            correct = right_order(v1, v2)
        if correct == True:
            return True
        elif correct == False:
            return False

    # Left has less items than right
    if len(s1) < len(s2):
        return True
    # Left has more items than right
    if len(s1) > len(s2):
        return False

    # Use None as a way of saying we aren't sure the order is correct, but at this depth and below, they are
    return None


total = 0
packets = []
for i in range(0, len(lines), 3):
    # print(f"index={i}")
    packets.append(eval(lines[i]))
    packets.append(eval(lines[i + 1]))
    if right_order(packets[-2], packets[-1]) in [True, None]:
        # print(f"good={i//3+1}")
        total += i // 3 + 1
print(total)

packets.append([[2]])
packets.append([[6]])

for i in range(0, len(packets)):
    for j in range(0, len(packets) - 1 - i):
        if right_order(packets[j], packets[j + 1]) == False:
            tmp = packets[j]
            packets[j] = packets[j + 1]
            packets[j + 1] = tmp

# print("\n".join(str(packet) for packet in packets))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
