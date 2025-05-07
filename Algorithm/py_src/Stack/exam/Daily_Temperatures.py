def dailyTemperatures(temperatures):
    stack = []  # 인덱스 저장
    answer = [0] * len(temperatures)

    for day in range(len(temperatures)):
        # 스텍이 비거나 스택의 마지막 온도가 현재 온도보다 커질 때까지 스텍에서 pop
        while stack and temperatures[stack[-1]] < temperatures[day]:
            prevDay = stack.pop()
            answer[prevDay] = day - prevDay
        stack.append(day)

    return answer


# 테스트
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures([30, 40, 50, 60]))
print(dailyTemperatures([30, 60, 90]))
