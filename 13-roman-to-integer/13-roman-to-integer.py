class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        i =0
        while i < len(s):
            if s[i] == "I" and i+1 < len(s):
                if s[i+1] == "V" or s[i+1] =="X":
                    result += (romans[s[i+1]] - romans[s[i]])
                    i = i+1
                else:
                    result += romans[s[i]]
            elif s[i] == "X" and i+1 < len(s):
                if s[i+1] == "L" or s[i+1] =="C":
                    result += (romans[s[i+1]] - romans[s[i]])
                    i = i+1
                else:
                    result+= romans[s[i]]
            elif s[i] == "C" and i+1 < len(s):
                if s[i+1] == "D" or s[i+1] =="M":
                    result += (romans[s[i+1]] - romans[s[i]])
                    i = i+1
                else:
                    result+= romans[s[i]]
            else:
                result += romans[s[i]]
            i+=1
            #print(result)
        return result
                