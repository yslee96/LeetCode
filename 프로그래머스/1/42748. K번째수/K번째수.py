def solution(array, commands):
    return list(sorted(array[left-1:right])[idx-1] for left, right, idx in commands)