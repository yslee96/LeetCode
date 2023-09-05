class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [-1 for _ in range(len(s))]
        def get_min_extra_num(idx):
            #print("call: ", idx)
            if idx>=len(s):
                return 0
            if dp[idx]!=-1:
                #print("cached: ", idx)
                return dp[idx]
            
            min_extra_num = len(s)
            string = ''
            for i in range(idx, len(s)):
                string += s[i]
                add = len(string)
                if string in dictionary:
                    add = 0
                #print(string, add, i)
                ret = get_min_extra_num(i+1)
                #print("return: ", ret)
                min_extra_num = min(min_extra_num, add + ret)
            #print("stored: ", idx, " value: ", min_extra_num)
            dp[idx] = min_extra_num
            return dp[idx]
     
        return get_min_extra_num(0)
        
        