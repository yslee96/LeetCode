class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2_dict = {}
        answer = []
        for word in words2:
            word_dict = {}
            for ch in word:
                if ch in word_dict:
                    word_dict[ch] +=1
                else:
                    word_dict[ch] = 1
            for key in word_dict:
                if key in word2_dict:
                    word2_dict[key] = max(word_dict[key], word2_dict[key])
                else:
                    word2_dict[key] = word_dict[key]
        for word in words1:
            flag = True
            word_dict = {}
            for ch in word:
                if ch in word_dict:
                    word_dict[ch] +=1
                else:
                    word_dict[ch] = 1
            for key in word2_dict:
                if key not in word_dict or word_dict[key] < word2_dict[key]:
                    flag = False
                    break
            if(flag):
                answer.append(word)
        return answer   
