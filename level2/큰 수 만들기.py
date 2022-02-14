def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    # print(''.join(answer[:len(answer) - k]))
    return ''.join(answer[:len(answer) - k])

number = "1231234"
k = 3
solution(number, k)
