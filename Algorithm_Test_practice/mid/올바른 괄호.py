def solution(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack or stack.pop() != "(":
                return False

    return not stack

# 테스트
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))