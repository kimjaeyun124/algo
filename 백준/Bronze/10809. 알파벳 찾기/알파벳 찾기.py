# ai 도움 받음
li = [-1] * 26
a = input()

for i in range(len(a)):
    index = ord(a[i]) - 97
    if li[index] == -1:
        li[index] = i
for x in li:
    print(x, end = " ")