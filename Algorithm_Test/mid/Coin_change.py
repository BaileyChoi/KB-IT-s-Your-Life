from collections import deque

def solution(coins, amount):
    # BFS로 최소 동전수 구하기
    queue = deque()
    visited = [False] * (amount + 1)

    # 시작점 예약 (cur, count)
    queue.append((0, 0))
    visited[0] = True

    # while queue:
    while queue:
        # 현재 노드 방문
        cur, count = queue.popleft()

        # if cur == amount: return count
        if cur == amount:
            return count

        # 다음 노드 방문
        for coin in coins:
            next = cur + coin
            if next <= amount and not visited[next]:
                queue.append((next, count + 1))
                visited[next] = True

    return -1

# 테스트
print(solution([1, 2, 5], 11))
print(solution([2], 3))
print(solution([1], 0))
