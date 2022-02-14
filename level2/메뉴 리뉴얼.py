from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            com = combinations(sorted(order), c)
            temp += com
        counter = Counter(temp)
        if counter:
            max_ = max(list(counter.values()))
            if max_ >= 2:
                for key, value in counter.items():
                    if counter[key] == max_:
                        answer.append(''.join(key))
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
solution(orders, course)