from collections import deque

def solution(places):
    answer = []

    # def bfs: 거리두기가 지켜지고 있는지 확인
    def bfs(start, board):   
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]

        queue = deque()
        visited = [[False] * 5 for _ in range(5)]

        # 시작점 예약
        queue.append((start, 0))
        visited[start[0]][start[1]] = True

        while queue:
            # 현재 노드 방문
            (curR, curC), dist = queue.popleft()

            # if 시작점이 아닌데 'P'를 만났고 거리가 2 이하라면 위반
            if dist != 0 and board[curR][curC] == 'P' and dist <= 2:
                return False
            
            # if 거리 2 초과면 cotinue
            if dist >= 2:
                continue

            # 다음 노드 방문
            for i in range(4):
                nextR, nextC = curR + dr[i], curC + dc[i]

                if 0 <= nextR < 5 and 0 <= nextC < 5 and board[nextR][nextC] != 'X':
                    if not visited[nextR][nextC]:
                        visited[nextR][nextC] = True
                        queue.append(((nextR, nextC), dist + 1))

        return True

    for room in places:
        is_valid = 1
        for row in range(5):
            for col in range(5):
                if room[row][col] == 'P':
                    if not bfs((row, col), room):
                        is_valid = 0
                        break
            if is_valid == 0:
                break

        answer.append(is_valid)

    return answer

# 테스트
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))