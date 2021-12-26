# no
def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left_s = '*'
    right_s = '#'
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left_s = i

        elif i in [3, 6, 9]:
            answer += 'R'
            right_s = i

        else:
            curPos = dic[i]
            lPos = dic[left_s]
            rPos = dic[right_s]
            left_d = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            right_d = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if left_d < right_d:
                answer += 'L'
                left_s = i

            elif left_d > right_d:
                answer += 'R'
                right_s = i

            else:
                if hand == 'left':
                    answer += 'L'
                    left_s = i

                else:
                    answer += 'R'
                    right_s = i

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
answer = solution(numbers, hand)
print(answer)