from collections import deque

def solution(maps):
    rowLen = len(maps)
    colLen = len(maps[0])

    # 시작지점, 레버, 출구 위치 찾기
    for r in range(rowLen):
        for c in range(colLen):
            if maps[r][c] == 'S':
                S = (r, c)
            elif maps[r][c] == 'L':
                L = (r, c)
            elif maps[r][c] == 'E':
                E = (r, c)

    def bfs(start, end):
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]

        queue = deque()
        visited = set()

        # 시작 노드 예약
        queue.append((start, 0))
        visited.add(start)

        while queue:
            # 현재 노드 방문
            (curR, curC), dist = queue.popleft()

            if (curR, curC) == end:
                return dist

            # 다음 노드 예약
            for i in range(4):
                nextR, nextC = curR + dr[i], curC + dc[i]
                if 0 <= nextR < rowLen and 0 <= nextC < colLen and maps[nextR][nextC] != 'X':
                    if (nextR, nextC) not in visited:
                        visited.add((nextR, nextC))
                        queue.append(((nextR, nextC), dist + 1))

        return -1

    # BFS로 시작 지점에서 레버까지의 거리 구하기
    distSL = bfs(S, L)

    # BFS로 레버에서 통로까지의 거리 구하기
    distLE = bfs(L, E)
    
    # 구한 두 거리 합하기
    return distSL + distLE if distSL != -1 and distLE != -1  else -1

# 테스트
print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
