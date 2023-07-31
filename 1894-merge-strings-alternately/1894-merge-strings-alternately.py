class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        idx1 = idx2 = 0
        ans = ''
        while idx1 < len(word1) or idx2 < len(word2):
            if idx1 < len(word1):
                ans += word1[idx1]
                idx1+=1
            if idx2 < len(word2):
                ans += word2[idx2]
                idx2+=1
            
        return ans
