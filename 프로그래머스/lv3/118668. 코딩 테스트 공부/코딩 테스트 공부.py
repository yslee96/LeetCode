def solution(alp, cop, problems):
    answer = 0
    dp = [[ float('inf') for _ in range(151)] for _ in range(151)]
    target_alp = target_cop = 0
    for problem in problems:
        target_alp = max(target_alp, problem[0])
        target_cop = max(target_cop, problem[1])
    
    # (주의1) 목표값이 초기값보다 더 작을 수도 있음
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)
    
    # (주의2) 시작점 세팅
    dp[alp][cop] = 0
    for i in range(alp,target_alp+1):
        for j in range(cop,target_cop+1):
            if i < target_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < target_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for k in range(len(problems)):
                if i >= problems[k][0] and j>=problems[k][1]:
                    next_alp = min(target_alp, i+problems[k][2])
                    next_cop = min(target_cop,j+problems[k][3])
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + problems[k][4])

                        
    return dp[target_alp][target_cop]
