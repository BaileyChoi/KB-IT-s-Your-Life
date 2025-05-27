import re


def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    answer = re.sub("[^a-z0-9\-_.]", "", answer)
    # 3단계
    answer = re.sub("\.+", ".", answer)
    # 4단계
    answer = answer.strip(".")
    # 5단계
    answer = "a" if len(answer) == 0 else answer
    # 6단계
    answer = answer[:15].rstrip(".") if len(answer) >= 16 else answer
    # 7단계
    answer = answer + answer[-1] * (3 - len(answer)) if len(answer) <= 2 else answer

    return answer


# 테스트
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
