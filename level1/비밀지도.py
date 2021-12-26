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


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n, arr1, arr2)
