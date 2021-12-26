def solution(n, lost, reserve):
    answer = 0
    for i in range(n+1):
        if i in lost:
            if i in reserve:
                reserve.remove(i)
                lost.remove(i)
    print(lost)
    print(reserve)
    for i in range(1, (n+1)):
        if i in lost:
            if(((i-1) in reserve)):
                lost.remove(i)
                reserve.remove(i-1)
            elif(((i+1) in reserve)):
                lost.remove(i)
                reserve.remove(i+1)
    answer = n - len(lost)

    return answer

n = 5
lost = [1, 2, 3, 4, 5]
reserve = [1, 2, 3]
answer = solution(n, lost, reserve)
print(answer)