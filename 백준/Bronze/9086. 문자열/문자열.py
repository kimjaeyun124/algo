a = int(input())
li = []
for i in range(a):
    b = input()
    li.append(b)
for j in li:
    print(j[0] + j[-1])