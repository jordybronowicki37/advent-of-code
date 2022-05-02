file = open("input", "r")
# file = open("input_test", "r")
caves = []


def get_cave(name):
    for i in caves:
        if i.name == name:
            return i
    cave = Cave(name)
    caves.append(cave)
    return cave


class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []

        if name == "start" or name == "end":
            self.mode = name
        elif name.islower():
            self.mode = "small"
        else:
            self.mode = "big"


def search_routes(route):
    route = route.copy()
    routes = []
    small_caves_visited = [x for x in route if x.mode == "small"]

    if len(route) == 0:
        route.append(get_cave("start"))

    for i in route[-1].connections:
        # niet terug naar start
        if i.mode == "start":
            continue

        # eindig route bij end
        elif i.mode == "end":
            routes.append(new_route(route, i))

        # small caves in gaan als hij nog niet bezocht is
        elif i.mode == "small" and i not in small_caves_visited:
            routes.extend(search_routes(new_route(route, i)))

        # andere small caves overslaan
        elif i.mode == "small":
            continue

        # geen loops in caves
        elif len(route) > 3 and route[-3] == route[-1] and route[-2] == i:
            continue

        else:
            routes.extend(search_routes(new_route(route, i)))

    return routes


def new_route(route, new):
    route = route.copy()
    route.append(new)
    return route


for line in file:
    line = line.replace("\n", "").split("-")

    cave1 = get_cave(line[0])
    cave2 = get_cave(line[1])

    cave1.connections.append(cave2)
    cave2.connections.append(cave1)

print(len(search_routes([])))
