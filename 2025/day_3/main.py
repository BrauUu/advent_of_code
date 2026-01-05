from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / 'data.txt'

data = open(my_file)
total = 0

# FIRST PART SOLUTION
for banks in data.readlines():
    n1 = 0
    n2 = 0
    le = len(banks[:-1])
    for i in range(0, le, 1):
        battery_joltage = int(banks[i])
        if battery_joltage > n1 and i < le-1:
            n1 = battery_joltage
            n2 = 0
        elif battery_joltage > n2:
            n2 = battery_joltage
    total += int(f'{n1}{n2}')

total = 0

# SECOND PART SOLUTION
for banks in data.readlines():
    n = [0 for _ in range(0,12,1)]
    j = 0
    for i in range(0, len(banks[:-1]), 1):
        battery_joltage = int(banks[i])
        leftOptionsNum = len(banks[i+1:-1])
        while battery_joltage > n[j]:
            if battery_joltage > n[j-1] and j > 0 and leftOptionsNum > 11 - (j):
                n[j] = 0
                j -= 1
            else:
                n[j] = battery_joltage
        if j < 11:
            j += 1
    n = [str(v) for v in n]
    temp = ''.join(n)
    total += int(temp)

print(total)
data.close()