from collections import deque

def solution(n, vertex):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)

    # 시작점 예약
    queue.append(1)
    visited[1] = True
    distances[1] = 0

    while queue:
        # 현재 노드 방문
        cur = queue.popleft()

        # 다음 노드 예약
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                distances[next] = distances[cur] + 1

    max_distance = max(distances)
    return distances.count(max_distance)


# 테스트
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))