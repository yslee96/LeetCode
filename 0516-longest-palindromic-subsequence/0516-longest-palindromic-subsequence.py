from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(start, end):
            if start > end:
                return 0
            
            if start == end:
                return 1

            if s[start] == s[end]:
                return 2 + memo_solve(start+1, end-1)
            
            else:
                return max(memo_solve(start+1, end), memo_solve(start, end-1))
        return memo_solve(0, len(s)-1)
        