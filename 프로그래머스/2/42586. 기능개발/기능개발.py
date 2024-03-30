import math
from itertools import accumulate, groupby
def solution(progresses, speeds):
    finish_days = [ (100-progress+speed-1) // speed for progress, speed in zip(progresses, speeds)]
    return list(len(list(group)) for _, group in groupby(accumulate(finish_days, max)))