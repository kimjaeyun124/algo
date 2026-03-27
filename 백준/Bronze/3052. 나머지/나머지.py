li = []
count = 0

for i in range(10):
     li.append(int(input()))

for i in range(len(li)):
    li[i] %= 42

li.sort()

for i in range(len(li)):
    if i == 9:
        count += 1
        break
    if li[i] != li[i + 1]:
        count += 1

print(count)