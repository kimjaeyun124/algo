a = int(input())
li = []
result = []
result_str = ""

for i in range(a):
    li.append(input())

result = list(li[0])

for i in li:
    for z in range(len(result)):
        if result[z] != i[z]:
            result[z] = "?"

for i in range(len(result)):
    result_str += result[i]
print(result_str)
