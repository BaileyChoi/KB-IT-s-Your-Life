def solution(n, computers):
    answer = 0

    visited = [False] * n

    for i in range(0, n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1

    return answer


def dfs(graph, visited, curVertex):
    visited[curVertex] = True
    for nextVertex in range(len(graph)):
        if graph[curVertex][nextVertex] == 1 and not visited[nextVertex]:
            dfs(graph, visited, nextVertex)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
