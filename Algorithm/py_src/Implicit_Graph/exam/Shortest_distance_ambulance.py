from collections import deque


def solution(city):
    rowLen = len(city)
    colLen = len(city[0])

    visited = [[False] * colLen for _ in range(rowLen)]
    dist = [[0] * colLen for _ in range(rowLen)]

    bfs(city, 0, 0, visited, dist)

    return (
        dist[rowLen - 1][colLen - 1]
        if city[0][0] != 1 and city[rowLen - 1][colLen - 1] != 1
        else -1
    )


def bfs(city, r, c, visited, dist):
    rowLen = len(city)
    colLen = len(city[0])

    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    queue = deque()

    queue.append([r, c])
    visited[r][c] = True
    dist[r][c] = 1

    while queue:
        # 현재 노드 방문
        [curRow, curCol] = queue.popleft()

        # 다음 노드 방문
        for i in range(8):
            nextRow = curRow + dr[i]
            nextCol = curCol + dc[i]

            if (
                0 <= nextRow < rowLen
                and 0 <= nextCol < colLen
                and city[nextRow][nextCol] == 0
            ):
                if not visited[nextRow][nextCol]:
                    queue.append([nextRow, nextCol])
                    visited[nextRow][nextCol] = True
                    dist[nextRow][nextCol] = dist[curRow][curCol] + 1


# 테스트
print(solution([[0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 0]]))  # 4

print(solution([[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 1, 0], [0, 0, 0]]))  # 5

print(solution([[0, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 1]]))  # -1

print(solution([[1, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0]]))  # -1
