def solution(array, commands):
    answer = []
    for command in enumerate(commands):
        i = command[1][0]
        j = command[1][1]
        k = command[1][2]
        tempArray = array[i-1:j]
        tempArray.sort()
        k = tempArray[k-1]
        answer.append(k)
    print(answer)
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)