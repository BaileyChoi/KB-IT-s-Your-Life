def solution(participants, completion):
    participants.sort()
    completion.sort()

    for p, c in zip(participants, completion):
        if p != c:
            return p
        
    return participants[-1]

# 테스트
print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))