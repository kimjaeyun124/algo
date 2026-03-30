a = input()

if len(a) == 1:
    a = "0" +  a

original = a
current = a
sum_a = 0
count = 0

while True:
    count += 1
    sum_a = int(current[0]) + int(current[1])
    sum_a = str(sum_a)
    current = current[1] + sum_a[-1]
    if original == current:
        break

print(count)