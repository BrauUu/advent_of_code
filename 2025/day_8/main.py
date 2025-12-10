from pathlib import Path
from math import sqrt

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data.txt"

data = open(my_file)
lines = data.readlines()
allConnections = []
MAX_CONNECTIONS = 1000

for i in range(0, len(lines), 1):
    actualJunctionBox = lines[i]
    x1, y1, z1 = list(map(int, actualJunctionBox.split(',')))
    for j in range(i + 1, len(lines), 1):
        compJuctionBox = lines[j]
        x2, y2, z2 = list(map(int, compJuctionBox.split(',')))
        dist = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        allConnections.append((dist, i, j))

allConnections.sort(key=lambda connection: connection[0])
closestConnections = allConnections[:MAX_CONNECTIONS]

aggrConnections = []
for connection in closestConnections:
    flag = True
    x = 0
    i = 0
    while i < len(aggrConnections):
        aggrConnection = aggrConnections[i]
        if connection[1] in aggrConnection or connection[2] in aggrConnection:
            if flag:
                aggrConnection.add(connection[2])
                aggrConnection.add(connection[1])
                x = i
                flag = False
            else:
                aggrConnections[x].update(aggrConnection)
                aggrConnections.pop(i)
        i += 1
    if flag:
        aggrConnections.append(set({connection[1], connection[2]}))

aggrConnections.sort(key=len, reverse=True)
total = len(aggrConnections[0]) * len(aggrConnections[1]) * len(aggrConnections[2]) 
print(total)
 