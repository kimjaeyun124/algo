def result(f, g, h, i, j):
    return ((f ** 2) + (g ** 2) + (h ** 2) + (i ** 2) + (j ** 2)) % 10

a, b, c, d, e = map(int,input().split())
print(result(a, b, c, d, e))