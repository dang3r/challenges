from collections import defaultdict

instructions = [line.strip().split() for line in open("18.in").readlines()]
registers = defaultdict(lambda: 0)
last_sound = 0

def value(val):
    if len(val) == 1 and ord('a') <= ord(val) <= ord('z'):
        return registers[val]
    return int(val)

pos = 0
while True:
    inst = instructions[pos]
    cmd = inst[0]
    inc = 1
    if cmd == "set":
        reg, val = inst[1:]
        registers[reg] = value(val)
    elif cmd == "mul":
        reg, val = inst[1:]
        registers[reg] = registers[reg] * value(val)
    elif cmd == "add":
        reg, val = inst[1:]
        registers[reg] = registers[reg] + value(val)
    elif cmd == "mod":
        r1, val = inst[1:]
        registers[r1] = registers[r1] % value(val)
    elif cmd == "snd":
        r1 = inst[1]
        last_sound = registers[r1]
    elif cmd == "rcv":
        r1 = inst[1]
        if registers[r1] != 0:
            break
    elif cmd == "jgz":
        v1, v2 = inst[1:]
        if value(v1)  != 0:
            inc = value(v2)
    else:
        raise ValueError("instruction invalid!")
    pos += inc

print(last_sound)

p1_cnt = 0
def program(id, rcv, send):
    global p1_cnt
    registers = defaultdict(lambda: 0)
    registers['p'] = id
    def value(val):
        if len(val) == 1 and ord('a') <= ord(val) <= ord('z'):
            return registers[val]
        return int(val)

    pos = 0
    while pos < len(instructions):
        inst = instructions[pos]
        cmd = inst[0]
        inc = 1
        if cmd == "set":
            reg, val = inst[1:]
            registers[reg] = value(val)
        elif cmd == "mul":
            reg, val = inst[1:]
            registers[reg] = registers[reg] * value(val)
        elif cmd == "add":
            reg, val = inst[1:]
            registers[reg] = registers[reg] + value(val)
        elif cmd == "mod":
            r1, val = inst[1:]
            registers[r1] = registers[r1] % value(val)
        elif cmd == "snd":
            val = inst[1]
            send.append(value(val))
            if id == 1:
                p1_cnt += 1
        elif cmd == "rcv":
            while len(rcv) == 0:
                yield
            r1 = inst[1]
            val = rcv.pop(0)
            registers[r1] = val
        elif cmd == "jgz":
            v1, v2 = inst[1:]
            if value(v1) > 0:
                inc = value((v2))
        else:
            raise ValueError("instruction invalid!")
        pos += inc

p0b, p1b = [], []
p0, p1 = program(0, p0b, p1b), program(1, p1b, p0b)
while True:
    # Assumes programs only terminat eby being blocked on io and not by getting past the final instructions
    # If they could, you just need to catch stop_iterations
    p0.__next__()
    p1.__next__()
    if len(p0b) == len(p1b) == 0:
        break

print(p1_cnt)