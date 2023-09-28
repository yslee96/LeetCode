class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        while right < len(t):
            if t[right] == s[left]:
                left +=1
                if left == len(s):
                    return True
            right+=1
        return False
            