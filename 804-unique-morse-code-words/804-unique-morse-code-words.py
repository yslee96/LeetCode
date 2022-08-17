class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                 "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        results = set()
        for word in words:
            res = ""
            for ch in word:
                res += morses[ord(ch)-ord("a")]
            results.add(res)
        print(results)
        return len(results)
            