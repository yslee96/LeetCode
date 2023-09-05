
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1 for _ in range(len(s))]
        def check_if_break_possible(idx):
            #print("call: ", idx)
            if idx >= len(s):
                return 1
            if dp[idx]!=-1:
                return dp[idx] == 1
            
            string = ''
            result = False
            for i in range(idx, len(s)):
                string += s[i]
                if string in wordDict:
                    if check_if_break_possible(i+1):
                        dp[idx] = 1
                        return dp[idx]
            dp[idx]=0
            return dp[idx]

        ret = check_if_break_possible(0) == 1
        #print(dp)
        return ret
        