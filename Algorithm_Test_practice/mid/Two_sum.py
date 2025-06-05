def solution(nums, target):
    dict = {}

    for i in range(len(nums)):
        if nums[i] in dict:
            return [dict[nums[i]], i]
        else:
            remaining = target - nums[i]
            dict[remaining] = i

# 테스트
print(solution([2,7,11,15], 9))
print(solution([3,2,4], 6))
print(solution([3,3], 6))
