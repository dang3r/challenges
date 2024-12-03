import re


program = open("d3.in").read()
regex =r"mul\((\d{1,3}),(\d{1,3})\)" 

# P1
total = 0
matches = re.findall(regex, program, flags=re.DOTALL)
for op1, op2 in matches:
    total += int(op1)*int(op2)
print(total)

# P2
idx = 0
total = 0
enabled = True
while idx < len(program):
    if program[idx:idx+4] == "do()":
        enabled = True
        idx += 4
    elif program[idx:idx+7] == "don't()":
        enabled = False
        idx += 7
    else:
        match = re.match(regex, program[idx:idx+12], flags=re.DOTALL)
        if match:
            idx += len(match.group(0))
            if enabled:
                total +=  int(match.group(1))* int(match.group(2))
        else:
            idx += 1

print(total)

        
    