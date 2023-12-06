file = open("input", "r")

lines = file.readlines()
times = [int(t) for t in filter(None, lines[0].replace("\n", "").replace("Time:", "").split(" "))]
distances = [int(d) for d in filter(None, lines[1].replace("Distance:", "").split(" "))]
answer = None

for i in range(len(times)):
    max_time = times[i]
    distance_record = distances[i]
    sub_answer = 0

    for j in range(max_time):
        charge_time = j + 1
        race_time = max_time - charge_time
        if charge_time * race_time > distance_record:
            sub_answer += 1

    if not answer:
        answer = sub_answer
    else:
        answer *= sub_answer

print(answer)
