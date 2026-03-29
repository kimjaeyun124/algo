a = int(input())
li =[]
while True:
    b = int(input())
    if b == 0:
        break
    li.append(b)
for i in li:
    if (i % a) != 0:
        print(f"{i} is NOT a multiple of {a}.")
    else:
        print(f"{i} is a multiple of {a}.")