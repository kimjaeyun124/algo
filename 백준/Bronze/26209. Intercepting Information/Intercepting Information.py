a = input()
a = a.replace(" ", "")
b = True
for i in a:
    if i != "0" and i != "1":
        b = False
        break
if b:
    print("S")
else:
    print("F")