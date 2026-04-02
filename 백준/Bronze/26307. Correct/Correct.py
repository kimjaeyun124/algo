a, b = map(int, input().split())
if a != 9:
    a -= 9
    a *= 60
else:
    a = 0
print(a + b)