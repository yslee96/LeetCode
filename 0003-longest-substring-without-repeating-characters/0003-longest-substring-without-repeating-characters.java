class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int answer = 0;
        HashSet<Character> hs = new HashSet<>();
        for(int right = 0; right < s.length(); right++){
            while(hs.contains(s.charAt(right))){
                hs.remove(s.charAt(left));
                left+=1;
            }
            hs.add(s.charAt(right));
            answer = Math.max(answer, right-left+1);
        }
        return answer;
    }
}