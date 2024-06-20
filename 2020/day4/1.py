file = open("input", "r")
passport = {}
valid = 0

def check(value):
    print(value)
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
    return True

for line in file:
    if line == "\n":
        if check(passport):
            valid += 1
        passport = {}
    else:
        tags = line.split(" ")
        for i in tags:
            value_pair = i.split(":")
            passport[value_pair[0]] = value_pair[1]

print(valid)
