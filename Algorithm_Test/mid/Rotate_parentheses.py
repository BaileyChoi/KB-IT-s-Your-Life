def solution(s):
    answer = 0
    
    # def validString: 올바른 괄호 문자열인지 확인
    def validString(s):
        stack = []
        pairs = {')': '(', ']': '[', '}': "{"}
        for c in s:
            # if 열림 괄호일 경우:
            if c in pairs.values():
                stack.append(c)
            # else 닫힘 괄호일 경우:
            else:
                if not stack or stack.pop() != pairs[c]:
                    return False

        return not stack

    # for i in range(len(s))
    for i in range(len(s)):    
        # 왼쪽으로 회전
        new_string = s[i:] + s[:i]

        # if 올바른 괄호문일 경우: answer += 1
        if validString(new_string): 
            answer += 1

    return answer

# 테스트
print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
