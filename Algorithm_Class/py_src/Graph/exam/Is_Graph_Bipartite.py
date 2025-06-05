from collections import deque


def isBipartite(graph):
    n = len(graph)

    visited = [0] * n  # 0: 방문 X, 1: 그롭1, -1: 그룹2

    for i in range(n):
        if not visited[i]:
            if not bfs(graph, i, visited):
                return False

    return True


def bfs(graph, start, visited):
    queue = deque()

    queue.append(start)
    visited[start] = 1  # 시작 노드 그룹 1

    while queue:
        curNode = queue.popleft()

        for linkNode in graph[curNode]:
            if not visited[linkNode]:
                queue.append(linkNode)
                visited[linkNode] = -visited[curNode]  # 서로 다른 그룹 할당
            elif visited[linkNode] == visited[curNode]:  # 인접한데 같은 그룹일 경우
                return False

    return True


# 테스트
print(isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False
print(isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))  # True
