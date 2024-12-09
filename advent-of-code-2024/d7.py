lines = open("d7.in").read().splitlines()

import functools


@functools.lru_cache
def opers(num):
    if num == 2:
        return [["+"], ["*"], ["||"]]

    ops = opers(num - 1)
    new_ops = []
    for op in ops:
        new_ops.append(op + ["+"])
        new_ops.append(op + ["*"])
        new_ops.append(op + ["||"])
    return new_ops


total = 0
for line in lines:
    value, operands = line.split(":")
    operands = [int(oper) for oper in operands.split()]
    value = int(value)

    operators_list = opers(len(operands))
    for operators in operators_list:
        running_value = operands[0]
        for i in range(len(operators)):
            if operators[i] == "+":
                running_value = running_value + operands[i + 1]
            elif operators[i] == "*":
                running_value = running_value * operands[i + 1]
            elif operators[i] == "||":
                running_value = int(f"{running_value}{operands[i+1]}")

        if running_value == value:
            total += value
            break

print(total)
