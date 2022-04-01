def solution(id_list, report, k):
    # answer = [0 for i in range(len(id_list))]
    answer = {id: 0 for id in id_list}
    # 집합 선언
    report = set(report)
    # print("report: ", report)
    dicReports = {id: [] for id in id_list}
    for i in report:
        i = i.split(" ")
        dicReports[i[0]].append(i[1])
    # print(dicReports)

    sueCount = {id: 0 for id in id_list}
    # print(sueCount)
    for value in dicReports.values():
        # print(value)
        for a in value:
            sueCount[a] = sueCount[a] + 1
    # print(sueCount)

    # 신고당한 id, 신고당한 횟수
    for key, value in sueCount.items():
        # 신고당한 횟수가 k 이상이라면
        if value >= k:
            # dicReports를 돌며 신고당한 id인 value2에 key가 있는지 확인
            # 신고한 id, 신고당한 id
            for key2, value2 in dicReports.items():
                # 있다면
                if key in value2:
                    index = 0
                    # answer의 key에 맞는 key2를 넣어 1을 증가시키기
                    answer[key2] = answer[key2] + 1
    t = []
    for value in answer.values():
        t.append(value)
    print(t)
    return t

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(id_list, report, k)