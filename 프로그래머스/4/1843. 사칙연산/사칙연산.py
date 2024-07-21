def solution(arr):
    answer = -1
    n = (len(arr) + 1) // 2  # 숫자의 개수
    
    # DP 테이블 초기화
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp_max[i][i] = int(arr[2 * i])
        dp_min[i][i] = int(arr[2 * i])
    
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp_max[i][j], dp_min[i][j] = float('-inf'), float('inf')
            for k in range(i, j):
                op = arr[2 * k + 1]
                if op == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                elif op == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])                    
    
    return dp_max[0][n-1]