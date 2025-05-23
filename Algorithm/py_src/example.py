import sys
import os
from collections import deque

file_path = os.path.join(os.path.dirname(__file__), "example.txt")
sys.stdin = open(file_path, "r")

# 백준 입력값 처리
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

def solution(N, M, board):
    # red, blue 위치 찾기
    for x in range(N):
        for y in range(M):
            if board[x][y] == "R":
                rx, ry = (x, y)
            elif board[x][y] == "O":
                bx, by = (x, y)


    # queue에 시작점 예약 (red 좌표, blue 좌표, count)
    queue = deque()
    visited = set()

    queue.append([rx, ry, bx, by, 0])
    visited.add([rx, ry, bx, by])

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while queue:
        [rx, ry, bx, by, count] = queue.popleft()
        # if 10번 이하로 움직여서 빼낼 수 없을 경우 return 0
        if count > 10:
            return 0
        
        # if red가 구멍에 빠졌을 경우 return 1
        if board[rx][ry] == "O":
            return 1
        
        # 다음 위치 예약
            # if blue가 구멍에 빠졌을 경우 continue
            # if red, blue 위치가 같으면 조정
            # if 방문 여부 확인 후 예약과 방문 표시 
    
    return 0

print(solution(N, M, board))

