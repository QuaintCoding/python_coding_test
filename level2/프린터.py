def solution(priorities, location):
    answer = 0
    count = 0
    list = [(i, p) for i, p in enumerate(priorities)]
    while list:
        temp = list.pop(0)
        flag = True
        for i in list:
            if i[1] > temp[1]:
                flag = False
                break
        if flag:
            answer += 1
            if temp[0] == location:
                return answer
        else:
            list.append(temp)


priorities = [2, 1, 3, 2]
location = 2
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
solution(priorities, location)