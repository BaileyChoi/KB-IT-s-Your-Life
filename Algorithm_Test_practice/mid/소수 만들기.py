import math
from itertools import combinations

def solution(nums):
    answer = 0

    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    for a, b, c in combinations(nums, 3):
        if isPrime(a + b + c):
            answer += 1

    return answer

# 테스트
print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))