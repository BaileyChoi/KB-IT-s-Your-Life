from collections import deque

def solution(N, M, board):
    # 행:N, 열:M
    queue = deque()
    visited = set()

    dr = [0, 0, -1 , 1]
    dc = [-1, 1, 0, 0]

    # 구슬 굴리기
    def move(r, c, i):
        nr, nc = r, c
        
        while True:
            nr = nr + dr[i]
            nc = nc + dc[i]
            # if 벽인 경우:
            if board[nr][nc] == "#":
                nr -= dr[i]
                nc -= dc[i]
                break
            # if 구멍인 경우:
            if board[nr][nc] == "O":
                break

        return (nr, nc)

    # 빨간 구슬, 파란 구슬, 구멍 위치 찾기
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                rowR, colR = r, c
            elif board[r][c] == 'B':
                rowB, colB = r, c
            elif board[r][c] == 'O':
                rowO, colO = r, c

    # 시작점 예약 (빨강, 파랑, count)
    queue.append((rowR, colR, rowB, colB, 0))
    visited.add((rowR, colR, rowB, colB))

    while queue:
        # 현재 노드 방문
        rowR, colR, rowB, colB, count = queue.popleft()

        # if 횟수 > 10
        if count > 10:
            return 0
        
        # if 빨강이 구멍에 빠졌을 때
        if (rowR, colR) == (rowO, colO):
            return 1
        
        # 다음 노드 예약
        for i in range(4):
            nrowR, ncolR = move(rowR, colR, i)
            nrowB, ncolB = move(rowB, colB, i)

            # if 파랑이 구멍에 빠졌을 때
            if (nrowB, ncolB) == (rowO, colO):
                continue

            # if 빨강, 파랑이 같은 위치일때:
            if (nrowR, ncolR) == (nrowB, ncolB):
                # if 빨강이 파랑보다 더 늦게 도착했을 때:
                if abs(nrowR - rowR) + abs(ncolR - colR) > abs(nrowB - rowB) + abs(ncolB - colB):
                    nrowR, ncolR = rowR - dr[i], colR - dc[i]
                else:
                    nrowB, ncolB = rowB - dr[i], colB - dc[i]

            # if 방문하지 않았다면:
            if (nrowR, ncolR, nrowB, ncolB) not in visited:
                visited.add((nrowR, ncolR, nrowB, ncolB))
                queue.append((nrowR, ncolR, nrowB, ncolB, count + 1))


    return 0


# 테스트
print(solution(5, 5, [
    "#####",
    "#..B#",
    "#.#.#",
    "#RO.#",
    "#####"
]))
print(solution(7, 7, [
    "#######",
    "#...RB#",
    "#.#####",
    "#.....#",
    "#####.#",
    "#O....#",
    "#######"
]))
print(solution(7, 7, [
    "#######",
    "#..R#B#",
    "#.#####",
    "#.....#",
    "#####.#",
    "#O....#",
    "#######"
]))
print(solution(10, 10, [
    "##########",
    "#R#...##B#",
    "#...#.##.#",
    "#####.##.#",
    "#......#.#",
    "#.######.#",
    "#.#....#.#",
    "#.#.#.#..#",
    "#...#.O#.#",
    "##########"
]))
print(solution(3, 7, [
    "#######",
    "#R.O.B#",
    "#######"
]))
print(solution(10, 10, [
    "##########",
    "#R#...##B#",
    "#...#.##.#",
    "#####.##.#",
    "#......#.#",
    "#.######.#",
    "#.#....#.#",
    "#.#.##...#",
    "#O..#....#",
    "##########"
]))
print(solution(3, 10, [
    "##########",
    "#.O....RB#",
    "##########"
]))
