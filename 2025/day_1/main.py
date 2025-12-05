from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / 'data.txt'

data = open(my_file)
actualPosition = 50
count = 0
for line in data:
    value = int(line[1:]) % 100
    count += int(line[1:]) // 100
    if line[0] == 'L':
        temp = actualPosition - value
        if temp < 0:
            if actualPosition != 0:
                count += 1
            temp = 100 + temp
        actualPosition = temp
    elif line[0] == 'R':
        temp = actualPosition + value
        if temp > 100:
            if actualPosition != 100:
                count += 1
            temp = temp - 100
        actualPosition = temp
    if actualPosition == 0 or actualPosition == 100:
        count += 1
print(count)
data.close()