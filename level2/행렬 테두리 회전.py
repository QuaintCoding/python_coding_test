def solution(rows, columns, queries):
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1,y1,x2,y2 in queries:
        temp = array[x1 - 1][y1 - 1]
        minimum = temp
        for i in range(x1 - 1, x2 - 1):
            test = array[i + 1][y1 - 1]
            array[i][y1 - 1] = test
            minimum = min(minimum, test)

        for i in range(y1 - 1, y2 - 1):
            test = array[x2 - 1][i + 1]
            array[x2 - 1][i] = test
            minimum = min(minimum, test)

        for i in range(x2 - 1, x1 - 1, -1):
            test = array[i - 1][y2 - 1]
            array[i][y2 - 1] = test
            minimum = min(minimum, test)

        for i in range(y2 - 1, y1 - 1, -1):
            test = array[x1 - 1][i - 1]
            array[x1 - 1][i] = test
            minimum = min(minimum, test)

        array[x1 - 1][y1] = temp
        answer.append(minimum)

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows, columns, queries)