from pathlib import Path

ROOT_DIR = Path(__file__).parent
my_file = ROOT_DIR / "data_test.txt"

data = open(my_file)
freshCount = 0
mode = 1
intervals = []

# PART 1
# for line in data.readlines():
#     if line[:-1] == '':
#         mode = 2
#         continue

#     if mode == 1:
#         n1, n2 = map(int, line[:-1].split('-'))
#         intervals.append([n1,n2])

#     if mode == 2:
#         n = int(line[:-1])
#         for interval in intervals:
#             if n >= interval[0] and n <= interval[1]:
#                 freshCount += 1
#                 break

# PART 2
for line in data.readlines():
    if line[:-1] == "":
        break
    if mode == 1:
        n1, n2 = map(int, line[:-1].split("-"))
        flag = False
        for interval in intervals:
            if (
                n1 > interval[0]
                and n1 < interval[1]
                or n2 > interval[0]
                and n2 < interval[1]
            ):
                interval[1] = n2 if n2 > interval[1] else interval[1]
                interval[0] = n1 if n1 < interval[0] else interval[0]
                flag = True
                break
        if flag:
            i = 0
            while i < len(intervals):
                currentInterval = intervals[i]
                n1 = currentInterval[0]
                n2 = currentInterval[1]
                for interval in intervals:
                    if (
                        n1 > interval[0]
                        and n1 < interval[1]
                        or n2 > interval[0]
                        and n2 < interval[1]
                    ):
                        interval[1] = n2 if n2 > interval[1] else interval[1]
                        interval[0] = n1 if n1 < interval[0] else interval[0]
                        intervals.pop(i)
                i += 1

        else:
            intervals.append([n1, n2])
    
for interval in intervals:
    temp = interval[1] - interval[0] + 1
    freshCount += temp


print(freshCount)
data.close()
