file = open("input", "r")

CARD_LABELS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
hands = {'hc': [], 'op': [], 'tp': [], 'tk': [], 'fh': [], 'fok': [], 'fik': []}


def check_freq(x):
    f = {}
    for c in set(x):
        f[c] = x.count(c)
    return f


def sort_func(a, b):
    print(a)
    print(b)
    return 1


for line in file:
    hand = line.replace("\n", "").split(" ")
    freq = list(check_freq(hand[0]).values())
    freq.sort(reverse=True)

    if freq[0] == 5:
        hands['fik'].append(hand)
    elif freq[0] == 4:
        hands['fok'].append(hand)
    elif freq[0] == 3 and freq[1] == 2:
        hands['fh'].append(hand)
    elif freq[0] == 3:
        hands['tk'].append(hand)
    elif freq[0] == 2 and freq[1] == 2:
        hands['tp'].append(hand)
    elif freq[0] == 2:
        hands['op'].append(hand)
    else:
        hands['hc'].append(hand)

for v in hands.values():
    

