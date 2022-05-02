file = open("input", "r")
amounts = {}
rules = {}
first_letter = ""


def dict_add_or_create(dic, name, amount):
    if dic.get(name):
        dic[name] += amount
    else:
        dic[name] = amount


first = True
for line in file:
    line = line.replace("\n", "")

    if first:
        first_letter = line[0]
        for i in range(len(line)-1):
            name = line[i] + line[i+1]
            dict_add_or_create(amounts, name, 1)
    elif not line == "":
        rule_split = line.split(" -> ")
        rules[rule_split[0]] = rule_split[1]

    first = False
print(amounts)

for i in range(10):
    print("Busy with itteration: "+str(i+1))
    new_amounts = {}

    for i in amounts.keys():
        amount = amounts.get(i)
        rule = rules.get(i)
        dict_add_or_create(new_amounts, i[0]+rule, amount)
        dict_add_or_create(new_amounts, rule+i[1], amount)

    amounts = new_amounts.copy()


occurences = {}
for i in amounts.keys():
    amount = amounts.get(i)
    dict_add_or_create(occurences, i[1], amount)
dict_add_or_create(occurences, first_letter, 1)


most = 0
least = None
for i in occurences.values():
    if i > most:
        most = i

    if not least or i < least:
        least = i

print(occurences)
print(most - least)
