from collections import deque
import sys
import os

cur_dir = os.path.dirname(__file__)  # 현재 파이썬 파일이 있는 디렉토리
file_path = os.path.join(cur_dir, "example.txt")
sys.stdin = open(file_path, "r")
input = sys.stdin.readline

# 입력값 받기
N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
departRow, departCol = map(int, input().split())

# 승객 출발,도착지 저장
customer = {}
for i in range(M):
    cRow, cCol, cARow, cACol = list(map(int, input().split()))
    customer[(cRow - 1, cCol -1)] = (cARow-1, cACol-1)

answer = 0

# 남아있는 승객이 있다면 반복문 수행
while fuel > 0 and customer:
    # BFS로 현재 택시 위치로부터 승객까지의 최단거리 계산
    cand, usedFuel = getCust(departRow, departCol)
    if usedFuel > fuel or len(cand) == 0:
        answer = -1
        break
    # 최단거리를 기준으로 가장 높은 우선순위의 승객 위치로 택시 이동
    departRow, departCol = sorted(cand)[0]
    # 연료가 충분하다면 BFS로 승객을 도착지까지 이동시키고 연료를 보충
    fuel -= usedFuel
    cARow, cACol, usedFuel = arriveCust(departRow, departCol)
    if usedFuel > fuel:
        answer = -1
        break
    fuel += usedFuel
    departCol, departCol = cARow, cACol
# 이동 성공 여부에 따라 출력값 결정
if answer != -1:
    # 승객 이동시키기에 성공한다면 남은 연료 출력
    print(fuel)
else:
    # 실패한다면 -1 출력  
    print(-1)
    
# 테스트
print(answer)   # 14