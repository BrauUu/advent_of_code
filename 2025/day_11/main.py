from pathlib import Path
import re

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data.txt"

data = open(my_file)
lines = data.readlines()
pathsCount = 0

devicesConnections = {}

for line in lines:
    values = re.split(": |[ ]", line[:-1])
    devicesConnections[values[0]] = values[1:]

# PART 1
# queue = devicesConnections["you"].copy()
# while queue:
#     connection = queue.pop()
#     if connection == "out":
#         pathsCount += 1
#         continue
#     queue.extend(devicesConnections[connection])

queue = devicesConnections["svr"].copy()
paths = [["svr"] for _ in range(0, len(queue), 1)]
i = 0
while queue:
    connection = queue.pop()
    if connection == "out":
        path = paths.pop(i)
        if path.count('fft') and path.count('dac'):
            pathsCount += 1
        continue
    paths[i].append(connection)
    for g in range(0, len(devicesConnections[connection]) - 1, 1):
        paths.insert(i, paths[i].copy())
    queue.extend(devicesConnections[connection])

print(pathsCount)