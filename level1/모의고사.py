def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin1 = format(arr1[i], 'b')
        bin1 = bin1.rjust(n, '0');
        bin2 = format(arr2[i], 'b')
        bin2 = bin2.rjust(n, '0');
        arr3 = ""
        for j in range(n):
            if (bin1[j] == "1") or (bin2[j] == "1"):
                arr3 = arr3 + "#"
            else:
                arr3 = arr3 + " "
        answer.append(arr3)
    return answer

answers = [1,3,2,4,2]
solution(answers)