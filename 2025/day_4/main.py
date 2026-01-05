from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / 'data.txt'

data = open(my_file)
rollsCount = 0
lines = data.readlines()
for i in range(0, len(lines), 1):
    lines[i] = list(lines[i])

while(True):
    newRollsCount = 0
    for i in range(0,len(lines), 1):
        line = lines[i][:-1]
        for g in range(0, len(line), 1):
            cell = line[g]
            if cell == '@':
                neighbourRollsCount = 0
                if g < len(line) - 1 and lines[i][g+1] == '@':
                    neighbourRollsCount += 1
                if g < len(line) - 1 and i < len(lines) - 1 and lines[i+1][g+1] == '@':
                    neighbourRollsCount += 1
                if i < len(lines) - 1 and lines[i+1][g] == '@':
                    neighbourRollsCount += 1
                if g > 0 and i < len(lines) - 1 and lines[i+1][g-1] == '@':
                    neighbourRollsCount += 1
                if g > 0 and lines[i][g-1] == '@':
                    neighbourRollsCount += 1
                if g > 0 and i > 0 and lines[i-1][g-1] == '@':
                    neighbourRollsCount += 1
                if i > 0 and lines[i-1][g] == '@':
                    neighbourRollsCount += 1
                if i > 0 and g < len(line) - 1 and lines[i-1][g+1] == '@':
                    neighbourRollsCount += 1

                if neighbourRollsCount < 4:
                    newRollsCount += 1
                    lines[i][g] = 'X'

    if newRollsCount == 0:
        break
    rollsCount += newRollsCount


print(rollsCount)
data.close()