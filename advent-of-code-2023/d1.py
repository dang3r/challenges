lines = open("d1.in").read().splitlines()

numbers_to_val = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

# part 1
total = 0
for line in lines:
    digits = [int(char) for char in line if char in "0123456789"]
    num = digits[0] * 10 + digits[-1]
    total += num
print(total)

# part 2
total = 0
for line in lines:
    digits = []
    for i in range(len(line)):
        for idx, num in enumerate(numbers_to_val):
            if line[i : i + len(num)] == num:
                digits.append(numbers_to_val[num])
    total += digits[0] * 10 + digits[-1]
print(total)
