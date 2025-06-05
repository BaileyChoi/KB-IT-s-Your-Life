from collections import deque

def solution(n, m, hole):
    # 보드 생성
    board = [[0]* m for _ in range(n)]

    # 보드에 함정 표시
    for hr, hc in hole:
         board[hr - 1][hc - 1] = 1

    # BFS로 최단 거리 계산
    queue = deque()
    visited = set()

    # 시작점 예약 (curR, curC, jumped, time)
    queue.append((0, 0, 0, 0))
    visited.add((0, 0, 0))

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    # while queue:
    while queue:
        # 현재 노드 방문
        curR, curC, jumped, time = queue.popleft()

        # if 도착지 방문: return time
        if curR == n - 1 and curC == m - 1:
            return time

        # 다음 노드 예약
        for i in range(4):
            nextR, nextC = curR + dr[i], curC + dc[i]
            if 0 <= nextR < n and 0 <= nextC < m:
                if (nextR, nextC, jumped) not in visited and board[nextR][nextC] == 0:
                    visited.add((nextR, nextC, jumped))
                    queue.append((nextR, nextC, jumped, time + 1))
        
        # if 점프를 하지 않은 경우:
        if jumped == 0:
            for i in range(4):
                nextR, nextC = curR + dr[i] * 2, curC + dc[i] * 2
                if 0 <= nextR < n and 0 <= nextC < m:
                    if (nextR, nextC, 1) not in visited and board[nextR][nextC] == 0:
                        visited.add((nextR, nextC, 1))
                        queue.append((nextR, nextC, 1, time + 1))

    return -1

# 테스트
print(solution(4, 4, [[2, 3], [3, 3]]))
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))