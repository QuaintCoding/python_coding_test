def solution(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n - 1, 3)
        rev_base += str(mod)
    rev_base = rev_base.replace('2','4').replace('1', '2').replace('0','1')
    return rev_base[::-1]

