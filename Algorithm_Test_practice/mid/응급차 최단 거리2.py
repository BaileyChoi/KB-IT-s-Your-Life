from collections import deque

def solution(city):
    # BFS로 최단 거리 구하기
    m = len(city)
    n = len(city[0])

    queue = deque()
    visited = [[False] * n for _ in range(m)]

    # 시작점 확인    
    if city[0][0] == 1:
        return -1

    # 시작점 예약
    queue.append((0, 0, 0))
    visited[0][0] = True

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while queue:
        # 현재 노드 방문
        curR, curC, dist = queue.popleft()
        # if 도착점 도착:
        if curR == m - 1 and curC == n - 1:
            return dist - 1
        # 다음 노드 예약
        for i in range(4):
            nextR, nextC = curR + dr[i], curC + dc[i]
            if 0 <= nextR < m and 0 <= nextC < n and city[nextR][nextC] == 0:
                if not visited[nextR][nextC]:
                    visited[nextR][nextC] = True
                    queue.append((nextR, nextC, dist + 1))

    return -1

# 테스트
print(solution([
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0]
]))
print(solution([
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]))
print(solution([
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1]
]))
print(solution([
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]))