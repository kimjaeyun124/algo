a = int(input())
sum = 0
sc = 1
li = []
for i in range(a):
    b = input()
    for j in range(len(b)):
        if j == 0:
            if b[j] == "O":
                sum += sc
                sc += 1
        elif b[j] == "O":
            sum += sc
            sc += 1
        elif b[j] == "X":
            sc = 1
    li.append(sum)
    sc = 1
    sum = 0
for z in li:
    print(z)