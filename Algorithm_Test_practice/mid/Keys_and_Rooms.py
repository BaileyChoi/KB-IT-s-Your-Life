from collections import deque

def solution(rooms):
    n = len(rooms)

    queue = deque()
    visited = [False] * n

    queue.append(0)
    visited[0] = True

    while queue:
        room = queue.popleft()
        for key in rooms[room]:
            if key != room and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

# 테스트
print(solution([[1],[2],[3],[]]))
print(solution([[1,3],[3,0,1],[2],[0]]))