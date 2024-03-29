
def solution(arr):
    return [ arr[idx] for idx in range(len(arr)-1) if arr[idx]!=arr[idx+1] ] + [arr[-1]]