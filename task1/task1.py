import sys

n, m = int(sys.argv[1]), int(sys.argv[2])

arr = [i for i in range(1, n + 1)] * m
first_elem = arr[0]
last_elem = arr[1]
way_arr = []
i = 1
while first_elem != last_elem:
    i -= 1
    way_arr.append(str(arr[i]))
    i += m
    if i > len(arr):
        i -= len(arr)
    last_elem = arr[i - 1]


print(''.join(way_arr))
