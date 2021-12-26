def solution(s):
    answer = []
    result = ""

    if len(s) == 1:
        return 1
    for n in range (1, len(s)//2+1):
        count = 1
        temp = s[:n]
        for i in range(n, len(s), n):
            if s[i:i+n] == temp:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp
                temp = s[i:i+n]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + temp
        answer.append(len(result))
        result = ""
    return min(answer)

s = "abcabcabcabcdededededede"
solution(s)