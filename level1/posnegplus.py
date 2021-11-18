def solution(absolutes, signs):
    answer = 123456789
    plus = 0
    minus = 0
    for i in range(len(absolutes)):
        if signs[i]:
            plus += absolutes[i];
        else:
            minus += absolutes[i];
    answer = plus - minus

    return answer