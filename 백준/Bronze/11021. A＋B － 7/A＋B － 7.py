a = int(input())
li = []

for i in range(a):
    b, c = map(int, input().split())
    li.append(b + c)
for j in range(len(li)):
    print(f"Case #{j + 1}: {li[j]}")