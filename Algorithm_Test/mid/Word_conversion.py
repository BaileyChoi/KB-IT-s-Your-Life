from collections import deque

def solution(begin, target, words):
    # BFS로 최소 변환수 구하기
    queue = deque()
    visited = set()

    def canChange(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
            if count > 1:
                return False
        return True
            
    # 시작점 예약 (cur, count)
    queue.append((begin, 0))
    visited.add(begin)

    while queue:
        # 현재 노드 방문
        cur, count = queue.popleft()

        # if cur == target: return count
        if cur == target:
            return count
        
        # 다음 노드 예약
        for word in words:
            if word not in visited and canChange(cur, word):
                visited.add(word)
                queue.append((word, count + 1))

    return 0

# 테스트
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) 
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) 
