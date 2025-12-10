from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data_test.txt"

data = open(my_file)
lines = data.readlines()

# PART 1
# start = lines[0].index('S')
# splitsCount = 0

# beams = set([start])

# for line in lines[1:]:
#     queue = beams.copy()
#     beams.clear()
#     while queue:
#         beam = queue.pop()
#         if line[beam] == '.':
#             beams.add(beam)
#         elif line[beam] == '^':
#             splitsCount += 1
#             beams.add(beam + 1)
#             beams.add(beam - 1)

# print(splitsCount)

# PART 2
start = lines[0].index('S')
count = 0
queue = [(0, start)]

while queue:
    pos = queue.pop()
    if pos[0] >= len(lines) - 1:
        count += 1
        continue

    if lines[pos[0] + 1][pos[1]] == '.':
        queue.append((pos[0] + 1, pos[1]))
    elif lines[pos[0] + 1][pos[1]] == '^':
        queue.append((pos[0] + 1, pos[1] - 1))
        queue.append((pos[0] + 1, pos[1] + 1))

print(count) 
data.close()
