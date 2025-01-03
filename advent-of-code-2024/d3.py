import re


program = open("d3.in").read()

def original_solution():
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

            
def revised_solution(): 
    # Revise the solution to just regex for P2.
    # - Use regex for getting do() and don't() in addition to mul()
    # - findall returns a tuple where each element is a given capture group specified by ()
    #   if that group was not found an empty string is returned. Condition off of the match
    #   to determine what was found

    # P1 remains the same
    total = 0
    regex =r"mul\((\d{1,3}),(\d{1,3})\)" 
    matches = re.findall(regex, program, flags=re.DOTALL)
    for op1, op2 in matches:
        total += int(op1)*int(op2)
    print(total)

    # P2
    total = 0
    regex = r"(do\(\))|(don't\(\))|(mul\((\d{1,3}),(\d{1,3})\))"
    matches = re.findall(regex, program, flags=re.DOTALL)
    enabled = True
    for match in matches:
        if match[0]:
            enabled = True
        elif match[1]:
            enabled = False
        elif match[2]:
            op1, op2 = match[3], match[4]
            op1 = int(op1)
            op2 = int(op2)
            if enabled:
                total += op1*op2
    print(total)

original_solution()
revised_solution()
