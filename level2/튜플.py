import re
def solution(s):
    answer = []
    a = s.split(',{')
    a.sort(key=len)
    for j in a:
        # print("j:", j)
        numbers = re.findall("\d+", j)
        for k in numbers:
            if int(k) not in answer:
                answer.append(int(k))
    # print(answer)
    return answer
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
solution(s)