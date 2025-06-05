def build_graph_list(n, edges):
    graph = [[] for _ in range(n)]  # 각 노드에 대해 빈 리스트 초기화

    for a, b in edges:
        graph[a].append(b)  # a -> b
        graph[b].append(a)  # b -> a (양방향)

    return graph


n = 5
edges = [[0, 1], [0, 2], [1, 3], [1, 4]]

graph_list = build_graph_list(n, edges)
print(graph_list)
# 출력 예시: [[1, 2], [0, 3, 4], [0], [1], [1]]
