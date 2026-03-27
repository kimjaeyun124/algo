a = int(input())
li = list(map(int, input().split()))
sum = 0
z = max(li)

for i in range(len(li)):
    li[i] /= z
    li[i] *= 100
for j in li:
    sum += j

print(sum / a)