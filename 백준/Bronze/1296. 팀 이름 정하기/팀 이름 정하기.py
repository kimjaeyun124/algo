# 1296
name = input() # 이름 받음
count = int(input()) # 팀 이름 개수
team_name = [] # 팀 이름 리스트
for i in range(count): # 팀 이름 개수 만큼 반복
    team_name_input = input() # 팀 이름 받음
    team_name.append(team_name_input) # 팀 이름을 리스트에 추가

max_sc = -1 # 최대 점수 함수
max_team = "" # 최대 점수 팀 이름 함수
current_team = 0 # 최근 팀 점수
team_name.sort() # 팀 이름을 순서대로 정리

for i in team_name: # i에 팀 이름을 대입
    combined = i + name # 이름과 팀 이름을 합침
    L = combined.count("L") # L의 갯수
    O = combined.count("O") # O의 갯수
    V = combined.count("V") # V의 갯수
    E = combined.count("E") # E의 갯수
    current_team = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100 # 최근 점수를 지정
    if max_sc < current_team: # 최고 점수가 최근 점수 보다 작을 때 
        max_team = i # 최대 점수 팀 이름 지정
        max_sc = current_team # 최대 점수 지정
print(max_team) # 최고 점수 팀 이름 출력
