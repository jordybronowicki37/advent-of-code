file = open("2input", "r")
flight_plan = {}


def getRow(value):
    value = value.replace("F", "0").replace("B", "1")
    return int(value, 2)


def getSeat(value):
    value = value.replace("L", "0").replace("R", "1")
    return int(value, 2)


for i in range(128):
    flight_plan[i] = [0, 1, 2, 3, 4, 5, 6, 7]

for line in file:
    row = getRow(line[:7])
    seat = getSeat(line[7:])
    flight_plan[row].remove(seat)
    if not flight_plan[row]:
        flight_plan.pop(row)

rows = list(flight_plan.keys())
for j in rows:
    if not len(flight_plan[j]) == 1:
        flight_plan.pop(j)

for k in flight_plan.keys():
    print((k*8)+flight_plan[k][0])
