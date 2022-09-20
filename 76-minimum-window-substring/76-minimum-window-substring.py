class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -=1
            
            if missing == 0:
                #print(s[left:right])
                while left < right and need[s[left]] < 0:
                    need[s[left]]+=1
                    left+=1
                #print(s[left:right])    
                if not end or right - left <= end - start:
                    start, end = left, right
                    #print(s[start:end])
                    need[s[left]] +=1
                    missing +=1
                    left +=1
        
        return s[start:end]
                    