class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for ch in s:
            start = ord(ch) - ord("a")
            dp[start % 26] = max(dp[i] for i in range(max(start-k, 0), min(start+k+1,26))) + 1
        return max(dp)
        