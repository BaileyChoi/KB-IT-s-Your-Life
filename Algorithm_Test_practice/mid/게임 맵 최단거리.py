from collections import deque

def solution(maps):
    # BFS로 최단거리 구하기
    N = len(maps)
    M = len(maps[0])

    queue = deque()
    visited = [[False] * M for _ in range(N)]

    # 시작점 예약(curR, curC, dist)
    queue.append((0, 0, 1))
    visited[0][0] = True

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while queue:
        # 현재 노드 방문
        curR, curC, dist = queue.popleft()

        # if 도착지 방문: return dist
        if curR == N - 1 and curC == M - 1:
            return dist

        # 다음 노드 예약
        for i in range(4):
            nextR, nextC = curR + dr[i], curC + dc[i]
            if 0 <= nextR < N and 0 <= nextC < M and maps[nextR][nextC] == 1:
                if not visited[nextR][nextC]:
                    visited[nextR][nextC] = True
                    queue.append((nextR, nextC, dist + 1))
    return -1

# 테스트
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
maps = [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]
print(solution(maps))
