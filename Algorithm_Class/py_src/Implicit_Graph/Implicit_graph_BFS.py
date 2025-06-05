from collections import deque

def bfs(r, c):
    queue = deque()

    queue.append([r, c])
    visited[r][c] = True

    # queue가 비어있을 때까지 방문
    while queue:
        # 현재 노드 방문
        [curRow, curCol] = queue.popleft()
        print((curRow, curCol), end=" ")

        # 다음 노드 방문
        for i in range(8):
            nextRow = curRow + dr[i]
            nextCol = curCol + dc[i]
            if isValid(nextRow, nextCol):
                if not visited[nextRow][nextCol]:
                    queue.append([nextRow, nextCol])
                    visited[nextRow][nextCol] = True

def isValid(r, c):
    return 0 <= r < rowLength and 0 <= c <colLength and grid[r][c] == 1

grid = [
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
]

# 상 하 좌 우 좌상 우상 좌하 우하
dr = [-1, 1, 0, 0,-1,-1, 1, 1]  # 행 이동
dc = [ 0, 0,-1, 1,-1, 1,-1, 1]  # 열 이동

rowLength = len(grid)
colLength = len(grid[0])

visited = [[False] * colLength for _ in range(rowLength)] 

bfs(0, 0)