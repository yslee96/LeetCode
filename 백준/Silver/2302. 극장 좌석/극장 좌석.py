import sys
input = sys.stdin.readline
num_seats = int(input())
num_vips = int(input())
is_vip = [False for _ in range(num_seats+1)]
for _ in range(num_vips):
    vip_num = int(input())
    is_vip[vip_num] = True
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