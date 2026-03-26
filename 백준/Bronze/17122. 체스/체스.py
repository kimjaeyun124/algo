li = [[1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1]
]
result = []
c, d = 0, 0
result_count_1 = 0
result_count_2 = 0

a = int(input())
for i in range(a):
    x, y = input().split(" ")
    y = int(y)
    if x[0] == "A": c = 0
    elif x[0] == "B": c = 1
    elif x[0] == "C": c = 2
    elif x[0] == "D":  c = 3
    elif x[0] == "E": c = 4
    elif x[0] == "F": c = 5
    elif x[0] == "G": c = 6
    elif x[0] == "H": c = 7
    d = int(x[1]) - 1
    result_count_1 = li[c][d]

    c = (y - 1) // 8
    d = (y - 1) % 8
    result_count_2 = li[c][d]
    if result_count_1 == result_count_2:
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)