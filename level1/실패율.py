def solution(N, stages):
    answer = []
    totaluser = len(answer)
    percent = []
    for i in range(1,N+1):
        fail = 0
        reach = 0
        for j in stages:
            if j == i:
                fail = fail + 1
                reach = reach + 1
            elif j > i:
                reach = reach + 1
        if fail == 0:
            percent.append((i, 0))
        else:
            percent.append((i, (fail / reach)))

    answer = sorted(percent, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    print(answer)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)