class Solution:
    def reverseVowels(self, s: str) -> str:
        from collections import defaultdict
        is_vowel = defaultdict(lambda : False)
        for vowel in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            is_vowel[vowel] = True
        
        vowels = [s[i] for i in range(len(s)) if is_vowel[s[i]]]
        for i in range(len(s)):
            if is_vowel[s[i]]:
                s = s[:i] + vowels.pop() + s[i+1:]
        
        return s