from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)

    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]

    bfs(grid, 0, 0, visited, dist)

    return dist[n - 1][n - 1] if not grid[0][0] and visited[n - 1][n - 1] else -1

def bfs(grid, r, c, visited, dist):
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, 1, -1, 1, -1]
    n = len(grid)

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

            if 0 <= nextRow < n and 0 <= nextCol < n and grid[nextRow][nextCol] == 0:
                if not visited[nextRow][nextCol]:
                    queue.append([nextRow, nextCol])
                    visited[nextRow][nextCol] = True
                    dist[nextRow][nextCol] = dist[curRow][curCol] + 1

#테스트
print(shortestPathBinaryMatrix([[0,1],[1,0]]))  # 2

print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))  # 4

print(shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))  # -1
