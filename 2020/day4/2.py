file = open("2input", "r")
passport = {}
valid = 0


def check(value):
    # print(value)
    if value.get("byr") is None:
        return False
    if value.get("iyr") is None:
        return False
    if value.get("eyr") is None:
        return False
    if value.get("hgt") is None:
        return False
    if value.get("hcl") is None:
        return False
    if value.get("ecl") is None:
        return False
    if value.get("pid") is None:
        return False

    if 1920 > int(value["byr"]) or int(value["byr"]) > 2002:
        return False
    if 2010 > int(value["iyr"]) or int(value["iyr"]) > 2020:
        return False
    if 2020 > int(value["eyr"]) or int(value["eyr"]) > 2030:
        return False

    if value["hgt"].endswith("cm") or value["hgt"].endswith("in"):
        num = int(value["hgt"][:len(value["hgt"]) - 2])
        if value["hgt"].endswith("cm"):
            if 150 > num or num > 193:
                return False
        else:
            if 59 > num or num > 76:
                return False
    else:
        return False

    if not value["hcl"][0] == "#":
        return False
    else:
        accepted_values = "1234567890abcdef"
        color = value["hcl"][1:]
        for i in color:
            if i not in accepted_values:
                return False

    accepted_ecl = ["amb", "blu", "grn", "brn", "gry", "hzl", "oth"]
    if value["ecl"] not in accepted_ecl:
        return False

    if not len(value["pid"]) == 9:
        return False

    return True


for line in file:
    if line == "\n":
        if check(passport):
            print(passport["byr"])
            valid += 1
        passport = {}
    else:
        tags = line.split(" ")
        for i in tags:
            value_pair = i.split(":")
            passport[value_pair[0]] = value_pair[1].replace("\n", "")

print(valid)
