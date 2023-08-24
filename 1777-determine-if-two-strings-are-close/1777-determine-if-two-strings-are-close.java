class Solution {
    public boolean closeStrings(String word1, String word2) {
        
        int len1 = word1.length();
        int len2 = word2.length();

        if(len1 != len2) return false;

        Map<Character, Integer> w1 = new HashMap<>();
        Map<Character, Integer> w2 = new HashMap<>();
        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<Integer> b = new ArrayList<>();

        for(int i=0; i<len1; i++){
            w1.put(word1.charAt(i), 1+w1.getOrDefault(word1.charAt(i), 0));
        }

        for(int i=0; i<len2; i++){
            if(w1.containsKey(word2.charAt(i))){
                w2.put(word2.charAt(i), 1+w2.getOrDefault(word2.charAt(i), 0));
            }
            else{
                return false;
            }
        }
        
        a = new ArrayList(w1.values());
        b = new ArrayList(w2.values());

        Collections.sort(a);
        Collections.sort(b);

        return a.equals(b);
    }
}