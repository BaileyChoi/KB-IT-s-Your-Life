from collections import deque


def solution(n, m, hole):
    # 함정 위치 표시
    trap = [[0] * (m + 1) for _ in range(n + 1)]
    for h in hole:
        trap[h[0]][h[1]] = True

    visited = [[[False] * 2 for _ in range(m + 1)] for _ in range(n + 1)]
    queue = deque()

    visited[1][1][0] = True
    queue.append([1, 1, 0, 0])

    dir1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir2 = [[0, 2], [2, 0], [0, -2], [-2, 0]]

    while queue:
        [curRow, curCol, jumped, dist] = queue.popleft()

        # 목적지 도착했으면 거리 반환
        if curRow == n and curCol == m:
            return dist

        # 한 칸 이동하는 경우
        for i in range(4):
            nextRow = curRow + dir1[i][0]
            nextCol = curCol + dir1[i][1]

            if 1 <= nextRow <= n and 1 <= nextCol <= m and not trap[nextRow][nextCol]:
                if not visited[nextRow][nextCol][jumped]:
                    queue.append([nextRow, nextCol, jumped, dist + 1])
                    visited[nextRow][nextCol][jumped] = True

        # 점프 뛰지 않았을 때의 점프 뛰는 경우
        if jumped == 0:
            for i in range(4):
                nextRow = curRow + dir2[i][0]
                nextCol = curCol + dir2[i][1]

                if (
                    1 <= nextRow <= n
                    and 1 <= nextCol <= m
                    and not trap[nextRow][nextCol]
                ):
                    if not visited[nextRow][nextCol][1]:
                        queue.append([nextRow, nextCol, 1, dist + 1])
                        visited[nextRow][nextCol][1] = True

    return -1


# 테스트
print(solution(4, 4, [[2, 3], [3, 3]]))

print(
    solution(
        5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]
    )
)
