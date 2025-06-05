def solution(n, computers):
    answer = 0

    def dfs(cur, visited, computers):
        visited[cur] = True
        for next in range(n):
            if computers[cur][next] == 1 and not visited[next]:
                dfs(next, visited, computers)

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers) 
            answer += 1

    return answer

# 테스트
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
