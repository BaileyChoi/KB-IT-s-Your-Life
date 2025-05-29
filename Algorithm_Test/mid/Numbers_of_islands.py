def solution(grid):
    answer = 0

    rowLen = len(grid)
    colLen = len(grid[0])

    visited = [[False] * colLen for _ in range(rowLen)]

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    def dfs(r, c):
        visited[r][c] = True

        for i in range(4):
            nextR, nextC = r + dr[i], c + dc[i]
        
            if 0 <= nextR < rowLen and 0 <= nextC < colLen and grid[nextR][nextC] == "1":
                if not visited[nextR][nextC]:
                    dfs(nextR, nextC)

    for i in range(rowLen):
        for j in range(colLen):
            if not visited[i][j] and grid[i][j] == "1":
                dfs(i, j)
                answer += 1

    return answer


# 테스트
print(solution([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(solution([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))