from collections import deque


def solution(begin, target, words):
    queue = deque()
    visited = set()

    queue.append((begin, 0))

    while queue:
        curWord, steps = queue.popleft()

        # target 단어 찾았을 경우
        if curWord == target:
            return steps

        # 다음 단어 탐색
        for nextWord in words:
            if nextWord not in visited and getDiffCount(curWord, nextWord) == 1:
                queue.append((nextWord, steps + 1))
                visited.add(nextWord)

    return 0


def getDiffCount(w1, w2):
    diffCount = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diffCount += 1
    return diffCount


# 테스트
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
