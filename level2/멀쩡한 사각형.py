import math

def solution(w, h):
    total = w * h
    minus = w + h - math.gcd(w, h)

    answer = total - minus
    #print(answer)
    return answer

W = 8
H = 12
solution(W, H)
