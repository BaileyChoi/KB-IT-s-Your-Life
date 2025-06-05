from collections import deque


def solution(n, edge):
    # 인접 리스트로 변환
    graph = [[] for _ in range(n + 1)]

    # 간선 추가
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    return bfs(graph, n)


def bfs(graph, size):
    queue = deque()
    visited = [False] * (size + 1)
    distance = [0] * (size + 1)

    queue.append(1)
    visited[1] = True
    distance[1] = 0

    while queue:
        curVertex = queue.popleft()
        for nextVertex in graph[curVertex]:
            if not visited[nextVertex]:
                queue.append(nextVertex)
                visited[nextVertex] = True
                distance[nextVertex] = distance[curVertex] + 1

    # 가장 먼 거리 구하기
    maxDistance = max(distance)

    # 가장 먼 거리를 가진 노드의 개수 구하기
    count = distance.count(maxDistance)

    return count


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
