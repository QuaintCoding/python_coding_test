def solution(lottos, win_nums):
    count = 0
    correct = 0

    for i in lottos:
        if(i == 0):
            count += 1
    for i in lottos:
        for j in win_nums:
            if(i == j):
                correct += 1
    max = 7 - (correct+count)
    min = 7 - correct
    if min >= 6:
        min = 6
    if(max >= 6):
        max = 6
    answer = [max, min]
    return answer

lottos = [38, 19, 20, 40, 15, 25]
win_nums = [38, 19, 20, 40, 15, 25]
a = solution(lottos, win_nums)
print(a)