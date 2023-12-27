import sys
from bisect import bisect_left
input = sys.stdin.readline

num_strings = int(input())
strings = [list(map(int, input().split())) for _ in range(num_strings)]
strings.sort()
string_b = [string[1] for string in strings]

if num_strings == 1:
    print(1)
else:
    dp = [string_b[0]]
    for string in string_b[1:]:
        if dp[-1] < string:
            dp.append(string)
        else:
            idx = bisect_left(dp, string)
            dp[idx] = string
    print(num_strings-len(dp))
