class Solution {
    public int bestClosingTime(String customers) {
        Map<Character, Integer> hs = new HashMap<>();
        for(char ch : customers.toCharArray()){
            hs.put(ch, hs.getOrDefault(ch, 0) + 1);
        }
        int len = customers.length();
        int [] penalties = new int[len+1];
        penalties[0] = hs.getOrDefault('Y',0);
        
        int minP = penalties[0];
        int minIdx = 0;
        for(int i=1; i<=len; i++){
            if(customers.charAt(i-1)=='Y'){
                penalties[i] = penalties[i-1]-1;
                if(penalties[i] < minP){
                    minP = penalties[i];
                    minIdx = i;
                }
            }else{
                penalties[i] = penalties[i-1]+1;
            }
        }

        return minIdx;
    }
}