from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / 'data.txt'

data = open(my_file)
total = 0

for banks in data.readlines():
    n1 = 0
    n2 = 0
    l = len(banks[:-1])
    for i in range(0, l, 1):
        battery_joltage = int(banks[i])
        if battery_joltage > n1 and i < l-1:
            n1 = battery_joltage
            n2 = 0
        elif battery_joltage > n2:
            n2 = battery_joltage
    total += int(f'{n1}{n2}')
print(total)
data.close()