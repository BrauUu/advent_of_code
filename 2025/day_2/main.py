from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / 'data.txt'

data = open(my_file)


# FIRST PART SOLUTION
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

# SECOND PART SOLUTION
ranges = data.read().split(',')
total = 0

for my_range in ranges:
    startRange = int(my_range[:my_range.find('-')])
    endRange = int(my_range[my_range.find('-') + 1:]) + 1
    for my_id in range(startRange, endRange, + 1):
        strId = str(my_id)
        j = 2
        i = len(strId) // j
        while i > 0:
            flag = True
            sequence = strId[:i]
            for g in range(i, len(strId), i):
                idPart = strId[g:g+i]
                if idPart != sequence:
                    flag = False
                    break
            j += 1
            i = len(strId) // j
            if flag:
                total += my_id
                break
            
print(total)