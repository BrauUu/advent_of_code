from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data.txt"

data = open(my_file)
lines = data.readlines()

# FIRST PART SOLUTION
start = lines[0].index('S')
splitsCount = 0

beams = set([start])

for line in lines[1:]:
    queue = beams.copy()
    beams.clear()
    while queue:
        beam = queue.pop()
        if line[beam] == '.':
            beams.add(beam)
        elif line[beam] == '^':
            splitsCount += 1
            beams.add(beam + 1)
            beams.add(beam - 1)

print(splitsCount)

# SECOND PART SOLUTION
start = lines[0].index('S')
width = len(lines[0]) - 1
height = len(lines)

dp = [[0] * width for _ in range(height)]
dp[0][start] = 1

for line in range(height - 1):
    for col in range(width):
        cell = lines[line+1][col]
        v = dp[line][col]
        if v == 0:
            continue
        if cell == '.':
            dp[line+1][col] += v
        elif cell == '^':
            if col > 0:
                dp[line+1][col-1] += v
            if col < height:
                dp[line+1][col+1] += v

print(sum(dp[height-1]))
        