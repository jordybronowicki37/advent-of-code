file = open("input", "r")
amount = 0
for line in file:
    digits = line.replace("\n", "").split(" | ")[1].split(" ")
    lengte_digits = [2, 3, 4, 7]
    for i in digits:
        if len(i) in lengte_digits:
            amount += 1
print(amount)
