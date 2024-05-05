def solution(numbers, target):
    def dfs(cnt, cur_result):
        if cnt == len(numbers):
            if cur_result == target:
                return 1
            else:
                return 0
        ret = 0
        ret += dfs(cnt+1, cur_result+numbers[cnt])
        ret += dfs(cnt+1, cur_result-numbers[cnt])
        return ret

    return dfs(0,0)