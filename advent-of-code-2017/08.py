import re

instructions = [line.strip() for line in open("08.in").readlines()]
state = dict()
highest = 0

for inst in instructions:
    m = re.match(r'(?P<reg>[a-z]+) (?P<op>dec|inc) (?P<amt>-?\d+) if (?P<cond_reg>[a-z]+) (?P<cond_op>==|<=|>=|<|>|!=) (?P<cond_cmp_amt>-?\d+)', inst)
    if not m:
        print(f"Failed to match '{inst}'")
        break
    d = m.groupdict()
    reg = d["reg"]
    op = d["op"]
    amt = int(d['amt'])
    cond_reg = d['cond_reg']
    cond_op = d['cond_op']
    cond_cmp_amt = int(d['cond_cmp_amt'])

    if cond_op == "==":
        func = lambda reg, amt: state.get(reg, 0) == amt
    elif cond_op == "!=":
        func = lambda reg, amt: state.get(reg, 0) != amt
    elif cond_op == ">=":
        func = lambda reg, amt: state.get(reg, 0) >= amt
    elif cond_op == "<=":
        func = lambda reg, amt: state.get(reg, 0) <= amt
    elif cond_op == "<":
        func = lambda reg, amt: state.get(reg, 0) < amt
    elif cond_op == ">":
        func = lambda reg, amt: state.get(reg, 0) > amt
    else:
        print(f"Failed to identify op {cond_op}")
        break

    if func(cond_reg, cond_cmp_amt):
        if op == "inc":
            state[reg] = state.get(reg, 0) + amt
        elif op == "dec":
            state[reg] = state.get(reg, 0) - amt
        highest = max(highest, state[reg])

print(max(state.values()))
print(highest)