def solution(n, wires):
    min_diff = float('inf')

    # def dfs: 한 네트워크의 송전탑 개수 구하기
    def dfs(start, visited, graph):
        visited.add(start)
        count = 1
        for next in graph[start]:
            if next not in visited:
                count += dfs(next, visited, graph)
        return count

    # 전력망 네트워크 생성
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # 전선 끊기
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        # dfs로 송전탑 개수 구하기
        visited = set()
        count1 = dfs(a, visited, graph)
        count2 = n - count1
        
        # 전선 다시 연결
        graph[a].append(b)
        graph[b].append(a)

        # 최소 송전탑 개수의 차이 갱신
        diff = abs(count1 - count2)        
        min_diff = min(min_diff, diff)
    
    return min_diff

# 테스트
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))