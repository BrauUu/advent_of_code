from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / 'data.txt'

data = open(my_file)
ranges = data.read().split(',')
total = 0

for my_range in ranges:
    startRange = int(my_range[:my_range.find('-')])
    endRange = int(my_range[my_range.find('-') + 1:]) + 1
    for my_id in range(startRange, endRange, + 1):
        strId = str(my_id)
        firstPart = strId[:len(strId) // 2]
        lastPart = strId[(len(strId) // 2):]
        if firstPart == lastPart:
            total += my_id

print(total)