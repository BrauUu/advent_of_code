from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data.txt"

data = open(my_file)
lines = data.readlines()
values = []
totals = []
# FIRST PART SOLUTION
for line in lines:
    line = line[:-1]
    tempValues = list(map(lambda v: v.strip() ,filter(lambda v : True if v else False, line.split(' '))))
    values.append(tempValues)

for i in range(0, len(values[0]), 1):
    totals.append(0)
    signal = values[-1][i]
    for g in range(0, len(values) - 1, 1):
        value = int(values[g][i])
        if signal == '+':
            totals[i] += value
        elif signal == '*':
            totals[i] = value * (totals[i] if totals[i] != 0 else 1)

# SECOND PART SOLUTION
values = []
totals = []

tempList = []
for i in range(2, len(lines[0]) + 1, 1):
    tempValue = ''
    for g in range(0, len(lines) - 1 , 1):
        tempValue += f'{lines[g][-i]}'
    tempValue = tempValue.strip()
    if tempValue:
        tempList.append(tempValue)
    else:
        tempList.append(lines[-1][-i + 1])
        values.append(tempList)
        tempList = []   

tempList.append(lines[-1][0])
values.append(tempList)

for i in range(0, len(values), 1):
    totals.append(0)
    signal = values[i][-1]
    for g in range(0, len(values[i]) - 1, 1):
        value = int(values[i][g])
        if signal == '+':
            totals[i] += value
        elif signal == '*':
            totals[i] = value * (totals[i] if totals[i] != 0 else 1)


print(sum(totals))
data.close()
