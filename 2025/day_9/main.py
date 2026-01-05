from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data.txt"

data = open(my_file)
bricks = data.readlines()

maxArea = 0

# PART 1
# for i in range(0, len(bricks), 1):
#     brick1 = bricks[i]
#     x1, y1 = list(map(int, brick1.split(',')))
#     for brick2 in bricks[i+1:]:
#         x2, y2 = list(map(int, brick2.split(',')))
#         temp = abs((x1 - x2) + 1) * ((y1 - y2)+ 1)
#         if temp > maxArea:
#             maxArea = temp

# PART 2

def myFunc(line):
    count = 0
    for i in range(len(line)):
        cell = line[i]
        if (cell == '#' or cell == 'X') and (i == len(line) - 1 or line[i+1] == '.'):
            count += 1
    return count



y_coords = []
x_coords = []

for brick in bricks:
    x, y = list(map(int, brick.split(',')))
    if x not in x_coords:
        x_coords.append(x)
    if y not in y_coords:
        y_coords.append(y)

x_coords.sort()
y_coords.sort()

x_compressed = {}
y_compressed = {}

i = 0

while len(x_coords) or len(y_coords):
    if len(x_coords):
        x_compressed[x_coords.pop(0)] = i
    if len(y_coords):
        y_compressed[y_coords.pop(0)] = i
    i += 1

compressed_bricks = []
 
for brick in bricks:
    x, y = list(map(int, brick.split(',')))
    compressed_bricks.append((x_compressed[x], y_compressed[y]))

drawing = [['.'] * (len(x_compressed) + 1) for _ in range(len(y_compressed))]

p_x = None
p_y = None

for compressed_brick in compressed_bricks:
    x = compressed_brick[0]
    y = compressed_brick[1]
    drawing[y] = drawing[y][:x] + ['#'] + drawing[y][x+1:]
    if p_x is not None and p_x != x:
        xs = (x, p_x) if x < p_x else (p_x, x)
        diff = abs(x - p_x) - 1
        if diff:
            drawing[y] = drawing[y][:xs[0] + 1] + ['X'] * diff + drawing[y][xs[1]:]
    if p_y is not None and p_y != y:
        ys = (y, p_y) if y < p_y else (p_y, y)
        for i in range(ys[0] + 1, ys[1], 1):
            drawing[i][x] = 'X'

    p_x = x
    p_y = y

for i in range(0, len(drawing)):
    line = drawing[i]
    ind = -1
    while ind < len(line) - 1:
        ind += 1
        cell = line[ind]
        if (cell == 'X' and len(line) > ind + 1 and line[ind+1] == '.') or ((cell == '#' and len(line) > ind + 1 and line[ind+1] == '.') and (myFunc(line[ind+1:]) % 2 == 1)):
            end = None
            nextXInd = None
            nextHashInd = None

            if line[ind + 1:].count('X') > 0:
                nextXInd = line.index('X', ind + 1)
                end = nextXInd
            if line[ind + 1:].count('#') > 0:
                nextHashInd = line.index('#', ind + 1)
                if nextXInd is None or nextXInd > nextHashInd:
                    end = nextHashInd
            
            if end is None:
                break

            diff = abs(ind - end) - 1
            line = line[:ind + 1] + ['X'] * diff + line[end:]
            ind = end
    drawing[i] = line

for i in range(0, len(bricks), 1):
    brick1 = bricks[i]
    x1, y1 = list(map(int, brick1.split(',')))
    for brick2 in bricks[i+1:]:
        x2, y2 = list(map(int, brick2.split(',')))
        temp = temp = abs((x1 - x2) + 1) * ((y1 - y2)+ 1)
        if temp > maxArea:
            x1_compressed = x_compressed.get(x1)
            x2_compressed = x_compressed.get(x2)
            y1_compressed = y_compressed.get(y1)
            y2_compressed = y_compressed.get(y2)

            xt = (x1_compressed, x2_compressed) if x1_compressed < x2_compressed else (x2_compressed, x1_compressed)
            yt = (y1_compressed, y2_compressed) if y1_compressed < y2_compressed else (y2_compressed, y1_compressed)

            flag = False

            if drawing[yt[0]][xt[0]:xt[1]].count('.') != 0 or drawing[yt[1]][xt[0]:xt[1]].count('.') != 0:
                flag = True
            for j in range(yt[0], yt[1], 1):
                if drawing[j][xt[0]] == '.' or drawing[j][xt[1]] == '.':
                    flag = True
                    break
            
            if flag:
                break
            maxArea = temp

print(maxArea)