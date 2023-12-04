file = open("input", "r")

lines = file.readlines()
amount_of_cards = len(lines)
card_copies = {key: 1 for key in range(amount_of_cards)}
answer = 0

for i in range(amount_of_cards):
    line = lines[i]
    line = line.replace("\n", "")
    data = line.split(": ")[1].split(" | ")
    winning_numbers = list(filter(None, data[0].split(" ")))
    my_numbers = list(filter(None, data[1].split(" ")))
    points = 0

    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            points += 1

    for _ in range(card_copies[i]):
        for j in range(points):
            k = i + j + 1
            if k < amount_of_cards:
                card_copies[k] += 1

for value in card_copies.values():
    answer += value

print(answer)
