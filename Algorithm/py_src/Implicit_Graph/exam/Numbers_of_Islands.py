def numIslands(grid):
    count = 0

    rowLen = len(grid)
    colLen = len(grid[0])

    visited = [[False] * colLen for _ in range(rowLen)]

    for i in range(rowLen):
        for j in range(colLen):
            if not visited[i][j] and grid[i][j] == "1":
                dfs(grid, i, j, visited)
                count += 1

    return count

def dfs(grid, r, c, visited):
    dr = [-1, 1, 0, 0]
    dc = [0 , 0, -1, 1]

    rowLen = len(grid)
    colLen = len(grid[0])

    # 현재 노드 방문
    visited[r][c] = True

    # 다음 노드 방문
    for i in range(4):
        nextRow = r + dr[i]
        nextCol = c + dc[i]

        if 0 <= nextRow < rowLen and 0 <= nextCol < colLen and grid[nextRow][nextCol] == "1":
            if not visited[nextRow][nextCol]:
                dfs(grid, nextRow, nextCol, visited)


# 테스트
print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # 1

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # 3