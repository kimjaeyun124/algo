def result(x, y):
    return (x + y) * (x - y)

a, b = map(int, input().split())
print(result(a, b))