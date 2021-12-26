import math

def solution(progresses, speeds):
    answer = []
    stack = []
    count = 0
    maxday = -1
    for i in range(len(progresses)):
        day = math.ceil((100-progresses[i]) / speeds[i])
        if day > maxday:
            while len(stack) != 0:
                stack.pop()
                count = count + 1
            maxday = day
            stack.append(day)
            if count != 0:
                answer.append(count)
            count = 0
        else:
            stack.append(day)

    while len(stack) != 0:
        stack.pop()
        count = count + 1
    answer.append(count)

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
solution(progresses, speeds)