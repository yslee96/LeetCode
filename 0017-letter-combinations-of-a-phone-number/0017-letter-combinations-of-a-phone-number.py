class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {2:["a", "b", "c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 
            6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:['w','x','y','z']
        }
        results = []
        limit = len(digits)
        def get_combi(digit_cnt, letters):
            if digit_cnt == limit:
                results.append(letters)
                return
            
            for letter in num_dict[int(digits[digit_cnt])]:
                get_combi(digit_cnt+1, letters+letter)
        
        get_combi(0, '')
        return results if len(digits)>0 else []