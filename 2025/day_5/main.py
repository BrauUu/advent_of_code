from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data.txt"

data = open(my_file)
freshCount = 0
mode = 1
intervals = []

# FIRST PART SOLUTION
for line in data.readlines():
    if line[:-1] == '':
        mode = 2
        continue

    if mode == 1:
        start, end = map(int, line[:-1].split('-'))
        intervals.append([start,end])

    if mode == 2:
        n = int(line[:-1])
        for interval in intervals:
            if n >= interval[0] and n <= interval[1]:
                freshCount += 1
                break

# SECOND PART SOLUTIONON
freshCount = 0
mode = 1
intervals = []

for line in data.readlines():
    if line[:-1] == "":
        break
    if mode == 1:
        start, end = map(int, line[:-1].split("-"))
        intervals.append([start, end])

intervals.sort()
intervalsMerged = []

for start, end in intervals:
    if not intervalsMerged or start > intervalsMerged[-1][1]:
        intervalsMerged.append([start, end])
    else:
        intervalsMerged[-1][1] = max(end, intervalsMerged[-1][1])

for start, end in intervalsMerged:
    freshCount += (end - start) + 1

print(freshCount)
data.close()
