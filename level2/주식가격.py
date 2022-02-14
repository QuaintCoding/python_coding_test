def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            print(i , j)
            answer[j] = i - j
        stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    print(answer)

prices = [1, 2, 3, 2, 3]
solution(prices)