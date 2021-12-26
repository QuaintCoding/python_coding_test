def solution(clothes):
    classification = []
    for cloth in clothes:
        if cloth[1] in classification:
            print("있음")
            classification[cloth[1]] += 1
        else:
            print("없음")
            classification[cloth[1]] = 1
    print(classification)
    answer = 0
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)