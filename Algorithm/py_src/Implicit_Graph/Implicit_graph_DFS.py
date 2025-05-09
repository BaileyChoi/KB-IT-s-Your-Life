def dfs(r, c):
    # 현재 노드 방문
    visited[r][c] = True
    print((r, c), end=" ")

    # 다음 노드 방문
    for i in range(4):
        nextRow = r + dr[i]
        nextCol = c + dc[i]
        if (isValid(nextRow, nextCol)):
            if not visited[nextRow][nextCol]:
                dfs(nextRow, nextCol)

def isValid(r, c):
    return 0 <= r < rowLength and 0 <= c <colLength and grid[r][c] == 1

grid = [
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1]
]

# 상하좌우
dr = [-1, 1, 0,  0]  # 행 이동
dc = [0,  0, -1, 1]  # 열 이동

rowLength = len(grid)
colLength = len(grid[0])

visited = [[False] * colLength for _ in range(rowLength)] 

dfs(0, 0)