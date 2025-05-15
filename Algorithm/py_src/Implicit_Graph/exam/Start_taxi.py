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
departRow -= 1
departCol -= 1

# 승객 출발,도착지 저장
customer = {}
for i in range(M):
    cRow, cCol, cARow, cACol = list(map(int, input().split()))
    customer[(cRow - 1, cCol - 1)] = (cARow - 1, cACol - 1)

# 현재 택시 위치에서 승객까지의 최단거리
def getCust(r, c):
    queue = deque([(r, c, 0)])
    visited = set([(r, c)])
    candidate = []
    minDist = 1000000

    while queue:
        curRow, curCol, curDist = queue.popleft()
        if curDist > minDist:
            break
        if (curRow, curCol) in customer:
            if curDist < minDist:
                candidate = [(curRow, curCol)]
                minDist = curDist
            elif curDist == minDist:
                candidate.append((curRow, curCol))
        for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nextRow, nextCol, nextDist = curRow + dr, curCol + dc, curDist + 1
            if 0 <= nextRow < N and 0 <= nextCol < M and board[nextRow][nextCol] != 1:
                  if (nextRow, nextCol) not in visited:
                    queue.append((nextRow, nextCol, nextDist))
                    visited.add((nextRow, nextCol))

    return candidate, minDist

# 도착지까지 승객 이동
def arriveCust(r, c):
    cARow, cACol = customer[(r, c)]
    del customer[(r, c)]
    queue = deque([(r, c, 0)])
    visited = set([(r, c)])

    while queue:
        curRow, curCol, curDist = queue.popleft()
        if curRow == cARow and curCol == cACol:
            return curRow, curCol, curDist
        for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nextRow, nextCol, nextDist = curRow + dr, curCol + dc, curDist + 1
            if 0 <= nextRow < N and 0 <= nextCol < M and board[nextRow][nextCol] != 1:
                if (nextRow, nextCol) not in visited:
                    queue.append((nextRow, nextCol, nextDist))
                    visited.add((nextRow, nextCol))

    return cARow, cACol, 1000000

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
    departRow, departCol = cARow, cACol
# 이동 성공 여부에 따라 출력값 결정
if answer == -1:
    # 승객 이동시키기에 실패한다면 -1 출력 
    print(-1)
else:
    # 성공한다면 남은 연료 출력
    print(fuel)
    