groups = open("d4.in").read().split("\n\n")

minimum_keys = set(
    [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]
)


good = 0
valid = 0
for group in groups:
    tokens = group.split()
    values = dict(tuple(token.split(":")) for token in tokens)
    group_keys = set(values.keys())
    if minimum_keys <= group_keys:
        good += 1

        correct_birth_year = len(values["byr"]) == 4 and (
            1920 <= int(values["byr"]) <= 2002
        )
        correct_issue_year = len(values["iyr"]) == 4 and (
            2010 <= int(values["iyr"]) <= 2020
        )
        correct_expiration_year = len(values["eyr"]) == 4 and (
            2020 <= int(values["eyr"]) <= 2030
        )

        if values["hgt"].endswith("cm"):
            correct_height = 150 <= int(values["hgt"][:-2]) <= 193
        elif values["hgt"].endswith("in"):
            correct_height = 59 <= int(values["hgt"][:-2]) <= 76

        correct_hair_color = (
            values["hcl"].startswith("#")
            and len(values["hcl"]) == 7
            and set(values["hcl"][1:]) <= set("abcdef0123456789")
        )
        correct_eye_color = values["ecl"] in "amb blu brn gry grn hzl oth".split()
        correct_pid = len(values["pid"]) == 9 and set(values["pid"]) <= set(
            "0123456789"
        )

        if all(
            [
                correct_birth_year,
                correct_issue_year,
                correct_expiration_year,
                correct_height,
                correct_hair_color,
                correct_eye_color,
                correct_pid,
            ]
        ):
            valid += 1


print(good)
print(valid)
