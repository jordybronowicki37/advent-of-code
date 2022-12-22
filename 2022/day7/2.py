file = open("input", "r")


class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def __getitem__(self, item):
        return self.contents.__getitem__(item)

    def __iter__(self):
        return self.contents.__iter__()

    def getName(self):
        return self.name

    def getByName(self, name):
        for dirItem in self.contents:
            if dirItem.getName() == name:
                return dirItem
        return None

    def append(self, item):
        self.contents.append(item)

    def getSize(self):
        s = 0
        for dirItem in self.contents:
            s += dirItem.getSize()
        return s


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size


def getCurrentDir():
    route = nav.split("/")
    route.remove("root")
    current_dir = root
    for d in route:
        current_dir = current_dir.getByName(d)
    return current_dir


root = Directory("root")
allDirs = [root]
nav = "root"

for line in file:
    line = line.replace("\n", "")

    if "$ ls" in line:
        continue
    elif "$ cd " in line:
        line = line.replace("$ cd ", "")

        if line == "/":
            nav = "root"
        elif line == "..":
            navList = nav.split("/")
            navList.pop()
            nav = "/".join(navList)
        else:
            nav += "/" + line
    elif "dir " in line:
        line = line.replace("dir ", "")
        current = getCurrentDir()
        newDir = Directory(line)
        current.append(newDir)
        allDirs.append(newDir)

    else:
        spl = line.split(" ")
        current = getCurrentDir()
        current.append(File(spl[1], int(spl[0])))


maxSpace = 70_000_000
requiredSpace = 30_000_000
usedSpace = root.getSize()
neededSpace = usedSpace + requiredSpace - maxSpace

selectedDir = root
for s in allDirs:
    if neededSpace < s.getSize() < selectedDir.getSize():
        selectedDir = s

print(selectedDir.getSize())
