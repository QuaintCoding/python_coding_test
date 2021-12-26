# https://programmers.co.kr/learn/courses/30/lessons/42839/solution_groups?language=python3

from itertools import permutations

def solution(numbers):
    answer = 0
    length = len(numbers)
    templist = []
    for i in range(1, length+1):
        temp = list(permutations(numbers, i))
        for j in temp:
            number = ""
            for k in j:
                number += k
            number = int(number)
            if number not in templist:
                templist.append(number)
    # print(templist)
    for i in templist:
        flag = True
        if i != 0 and i != 1:
            # print("i", i)
            for q in range(2, (i//2+1)):
                # print("q", q)
                if (i % q) == 0:
                    # print("i", i)
                    flag = False
                    break
        else:
            flag = False
        if flag:
            answer += 1
    #print(answer)
    return answer

numbers = "17"
solution(numbers)
