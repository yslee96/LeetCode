class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = collections.Counter(list(ransomNote))
        mgz = collections.Counter(list(magazine))
        flag = True
        for letter in note:
            if mgz[letter] < note[letter]:
                return False
        return True
                
        