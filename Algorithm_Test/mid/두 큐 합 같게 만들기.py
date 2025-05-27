from collections import deque


def solution(queue1, queue2):
    # queue1, queue2 큐로 만들기
    q1 = deque(queue1)
    q2 = deque(queue2)

    # q1, q2의 초기 합 기록
    sum1 = sum(q1)
    sum2 = sum(q2)

    # for 최대 수행 횟수
    for i in range(4 * len(q1)):
        # if 두 큐 합이 같을 경우:
        if sum1 == sum2:
            return i

        # elif q1의 합이 더 클 경우:
        elif sum1 > sum2:
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value

        # else q2의 합이 더 클 경우:
        else:
            value = q2.popleft()
            q1.append(value)
            sum2 -= value
            sum1 += value

    return -1


# 테스트
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
