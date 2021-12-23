import sys

file_1 = open(sys.argv[1], 'r', encoding='UTF-8')
file_2 = open(sys.argv[2], 'r', encoding='UTF-8')

center = tuple(float(i) for i in file_1.readline().split())
r = float(file_1.readline())
for line in file_2.readlines():
    point = tuple(float(i) for i in line.split())
    if (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2 < r ** 2:
        print(1)
    elif (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2 > r ** 2:
        print(2)
    else:
        print(0)
file_1.close()
file_2.close()
