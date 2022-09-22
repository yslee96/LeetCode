class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        letters = {2: "abc", 3: "def", 4:"ghi", 5:"jkl", \
                    6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        def make_combi(digits:str, idx:int, cur:str):
            if idx == len(digits)+1:
                if cur != "":
                    results.append(cur)
                return
            
            for ch in letters[int(digits[idx-1])]:
                make_combi(digits, idx+1, cur+ch)
                
        
        make_combi(digits, 1, "")
        return results if len(results) else []