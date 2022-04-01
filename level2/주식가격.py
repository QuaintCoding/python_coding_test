def solution(prices):
    answer = [0] * len(prices)
    price_stack = []
    total_time = len(prices) - 1

    # prices를 다 돌기
    index = 0
    for price in prices:
        # 비어있으면 그냥 append
        if not price_stack:
            price_stack.append([price, index])
        else:
            # 만약 새로들어오는 price가 stack의 top 값보다 작다면
            if price < price_stack[-1][0]:
                # stack의 top 값이 price보다 크지 않도록 지속적으로 pop해줘야됨
                while price_stack and price < price_stack[-1][0]:
                    pop_value = price_stack.pop()
                    # print(pop_value[0], pop_value[1])
                    # time을 넣어야됨
                    answer[pop_value[1]] = total_time - pop_value[1] - (index - pop_value[1])
                    # print("answer", answer)

            # 마지막으로 새로운 price를 append
            price_stack.append([price, index])
        print("price_stack",price_stack)
        index += 1

    # stack에 남아있는 것들 모두 빼야됨
    while (price_stack != []):
        pop_value = price_stack.pop()
        # print(pop_value[0], pop_value[1])
        # time을 넣어야됨
        answer[pop_value[1]] = total_time - pop_value[1]

    # print(price_stack)
    return answer

def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    # stack에 index 0을 먼저 하나 넣어 둔다(1부터 비교)
    stack = [0]
    # 1부터 리스트의 마지막 index까지 반복문을 돌린다.
    for i in range(1, len(prices)):
        # stack이 있고 prices[(stack의 top index] 값이 prices[i]의 값보다 크다면
        # pop한 뒤 현재 index와 stack에서 pop된 index를 빼서 저장한다.
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        # 마지막으로 새로운 index를 append
        stack.append(i)
    # print(answer)
    return answer

prices = [1, 2, 3, 2, 3]
solution(prices)