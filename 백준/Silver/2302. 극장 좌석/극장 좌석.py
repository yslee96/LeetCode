import sys
input = sys.stdin.readline
num_seats = int(input())
num_vips = int(input())
is_vip = [False for _ in range(num_seats+1)]
for _ in range(num_vips):
    is_vip[int(input())] = True
dp = [0 for _ in range(num_seats+1)]
if num_seats == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(1, num_seats+1):
        if is_vip[i] or is_vip[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[num_seats])
    
"""
D[i] : VIP석 없이 1~i을 배치할 경우의 수
D[N]을 구하기 위해 N번 학생이 어디에 앉는지로 케이스를 나눠봅시다.
Case 1 - N번 학생이 N번 자리에 앉는 경우 : 1~N-1번 학생들을 잘 앉히면 되므로 D[N-1]
Case 2 - N번 학생이 N-1번 자리에 앉는 경우 : N-1번 학생은 반드시 N번 자리에 앉아야하고, 나머지 1~N-2번 학생들을 잘 앉히면 되므로 D[N-2]
"""