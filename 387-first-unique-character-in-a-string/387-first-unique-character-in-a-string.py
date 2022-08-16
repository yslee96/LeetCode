class Solution:
    def firstUniqChar(self, s: str) -> int:
        chs = {}
        for i in range(len(s)):
            if s[i] in chs:
                chs[s[i]] +=1
            else:
                chs[s[i]] =1
        
        for i in range(len(s)):
            if chs[s[i]] == 1:
                return i
        return -1