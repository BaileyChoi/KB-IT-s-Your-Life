from collections import deque
import sys
import os

file_path = os.path.join(os.path.dirname(__file__), "example.txt")
sys.stdin = open(file_path, "r")

# 백준 입력값 처리
N, M, K = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]


def solution(N, M, K, board):
    # BFS 최단거리 구하기
    queue = deque()
    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
    # 시작점 예약
    queue.append((0, 0, 1, 0))
    visited[0][0][0] = True

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while queue:
        # 현재 노드 방문
        curR, curC, dist, broke = queue.popleft()

        # if 도착지 방문: return dist
        if curR == N - 1 and curC == M - 1:
            return dist

        # 다음 노드 방문
        for i in range(4):
            nextR, nextC = curR + dr[i], curC + dc[i]
            if 0 <= nextR < N and 0 <= nextC < M:
                if board[nextR][nextC] == 0 and not visited[nextR][nextC][broke]:
                    queue.append((nextR, nextC, dist + 1, broke))
                    visited[nextR][nextC][broke] = True

                # 벽인데 부술 기회가 남아있는 경우
                elif (
                    board[nextR][nextC] == 1
                    and broke < K
                    and not visited[nextR][nextC][broke + 1]
                ):
                    queue.append((nextR, nextC, dist + 1, broke + 1))
                    visited[nextR][nextC][broke + 1] = True

    return -1


print(solution(N, M, K, board))
