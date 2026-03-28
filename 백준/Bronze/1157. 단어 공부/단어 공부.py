# ai활용

a = input() # 문자 입력
a = a.lower() # 문자를 모두 소문자로 변경
al = {} # dic 추가
a_max_key = ""
a_max_value = 0
for i in a:
    if not(i in al):
        al[i] = 1
    else:
        al[i] += 1
a_max_value = max(al.values())
k = []
for key, value in al.items():
    if value == a_max_value:
        k.append(key)
if len(k) > 1:
    print("?")
else:
    print(k[0].upper())