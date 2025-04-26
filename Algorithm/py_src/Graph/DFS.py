def dfs(graph, start_vertex, visited):
    visited.add(start_vertex)
    print(start_vertex, end=" ")

    for next_vertex in graph[start_vertex]:
        if next_vertex not in visited:
            dfs(graph, next_vertex, visited)


graph = [
    [1, 2],  # 0번 노드 → 1, 2
    [0, 3],  # 1번 노드 → 0, 3
    [0, 4],  # 2번 노드 → 0, 4
    [1],  # 3번 노드 → 1
    [2],  # 4번 노드 → 2
]

visited = set()
dfs(graph, 0, visited)
