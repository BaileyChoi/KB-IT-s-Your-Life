from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]  # 행 이동(상하좌우)
    dy = [0, 0, -1, 1]  # 열 이동(상하좌우)

    n = len(maps)  # 행 길이
    m = len(maps[0])  # 열 길이

    queue = deque()
    visited = [[False] * m for _ in range(n)]

    queue.append((0, 0))  # 시작점
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 갈 수 있는 길인지 확인
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

    return maps[n - 1][m - 1] if maps[n - 1][m - 1] != 1 else -1


# 테스트
print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
        ]
    )
)
