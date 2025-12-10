from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data.txt"

data = open(my_file)
bricks = data.readlines()

maxArea = 0

# PART 1
for i in range(0, len(bricks), 1):
    brick1 = bricks[i]
    x1, y1 = list(map(int, brick1.split(',')))
    for brick2 in bricks[i+1:]:
        x2, y2 = list(map(int, brick2.split(',')))
        temp = abs((x1 - x2) + 1) * ((y1 - y2)+ 1)
        if temp > maxArea:
            maxArea = temp

# PART 2


print(maxArea)
 