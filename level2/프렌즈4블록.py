# https://velog.io/@wisepine/Programmers-%ED%94%84%EB%A0%8C%EC%A6%884%EB%B8%94%EB%A1%9D-python
def solution(m, n, board):
    board = list(map(list, zip(*board)))
    print(board)

    def game(b):
        pops = 0
        sc = [i[:] for i in b]
        for i in range(1, n):
            for j in range(1, m):
                if b[i][j] == -1: continue
                if b[i][j] == b[i - 1][j] == b[i - 1][j - 1] == b[i][j - 1]:
                    sc[i][j], sc[i - 1][j], sc[i - 1][j - 1], sc[i][j - 1] = 0, 0, 0, 0

        for i, v in enumerate(sc):
            cnt = v.count(0)
            pops += cnt
            sc[i] = [-1] * cnt + [a for a in v if a != 0]

        return sc, pops

    answer = 0
    while True:
        board, pops = game(board)
        if pops == 0:  return answer
        answer += pops

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]