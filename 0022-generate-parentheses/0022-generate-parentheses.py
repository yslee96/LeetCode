class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        possibles = []
        ans = []
        def combination( cur_len, combi ):
            if cur_len == n*2:
                possibles.append(combi)
                return
            combi += '('
            combination(cur_len+1, combi)
            combi = combi[:-1]
            combi += ')'
            combination(cur_len+1, combi)
            
        combination(0, '')
        for string in possibles:
            valid = True
            stack = []
            for ch in string:
                if ch == '(':
                    stack.append('(')
                else:
                    if stack and stack[-1]=='(':
                        stack.pop()
                    else:
                        valid = False
                        break
            if valid and not stack:
                ans.append(string)
                
        return ans
                