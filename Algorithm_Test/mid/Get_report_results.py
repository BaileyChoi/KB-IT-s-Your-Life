def solution(id_list, report, k):
    # mail_dict 생성 (id: 메일 수)
    mail_dict = {id: 0 for id in id_list}

    # report_dict 생성 (id: repoter1, repoter2, ...)
    report_dict = {id: [] for id in id_list}

    # 중복 신고 제거
    report = set(report)

    # 신고 처리
    for r in report:
        reporter, target = r.split()
        report_dict[target].append(reporter)

    # 유저 정지, 메일 발송 처리
    for target, reporters in report_dict.items():
        if len(reporters) >= k:
            for reporter in reporters:
                mail_dict[reporter] += 1

    return list(mail_dict.values())


# 테스트
print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
)
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
