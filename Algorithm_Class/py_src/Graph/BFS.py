from collections import deque


def bfs(graph, start_vertex):
    queue = deque()
    visited = set()

    queue.append(start_vertex)
    visited.add(start_vertex)

    while queue:
        cur_vertex = queue.popleft()

        print(cur_vertex, end=" ")

        for next_vertex in graph[cur_vertex]:
            if next_vertex not in visited:
                queue.append(next_vertex)
                visited.add(next_vertex)


graph = [
    [1, 2],  # 0번 노드 → 1, 2
    [0, 3],  # 1번 노드 → 0, 3
    [0, 4],  # 2번 노드 → 0, 4
    [1],  # 3번 노드 → 1
    [2],  # 4번 노드 → 2
]

bfs(graph, 0)
