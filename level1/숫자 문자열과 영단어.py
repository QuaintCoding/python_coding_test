def solution(s):
    answer = 0
    english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(english)):
        s = s.replace(english[i], str(i))

    answer = int(s)
    return answer

s = "2three45sixseven"
answer = solution(s)
print(answer)