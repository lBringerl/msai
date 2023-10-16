def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(1, len(lst) - i):
            l, r = lst[j - 1], lst[j]
            if l > r:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
            # elif l < r:
            #     lst[j - 1], lst[j] = lst[j], lst[j - 1]


table = []
N = int(input())
for i in range(N):
    line = input().split()
    table.append((-int(line[1]), int(line[0]), line[2]))

print(table)
bubble_sort(table)
print(table)

for i in range(3):
    print(table[i][2])
for row in table:
    print(row[1], end=' ')
