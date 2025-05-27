def solution(d, budget):
    answer = 0

    d.sort()

    for money in d:
        budget -= money
        if budget >= 0:
            answer += 1
    
    return answer

# 테스트
print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))
