class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = collections.defaultdict(int)
        mgz = collections.defaultdict(int)
        for ch in ransomNote:
            note[ch] +=1
        for ch in magazine:
            mgz[ch] +=1
        flag = True
        for key, value in note.items():
            if mgz[key] and mgz[key] >= value:
                continue
            else:
                flag = False
        print(note.items())
        return flag
                
        