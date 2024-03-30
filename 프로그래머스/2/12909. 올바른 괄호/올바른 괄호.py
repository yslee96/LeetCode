from itertools import accumulate
def solution(s):
    result = list(accumulate(s, func=lambda x,y : x-1 if y=="(" else x+1, initial = 0))
    return 1 not in result and result[-1] == 0
