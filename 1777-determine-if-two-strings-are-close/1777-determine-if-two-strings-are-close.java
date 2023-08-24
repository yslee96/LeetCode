class Solution {
    public boolean closeStrings(String word1, String word2) {
        Map<Character, Integer> w1 = new HashMap<>();
        Map<Character, Integer> w2 = new HashMap<>();
        Map<Integer, Integer> f1 = new HashMap<>();
        Map<Integer, Integer> f2 = new HashMap<>();

        if(word1.length() != word2.length()){
            return false;
        }

        for(char ch : word1.toCharArray()){
            if(w1.containsKey(ch)){
                w1.put(ch, w1.get(ch) + 1);
            }else{
                w1.put(ch, 1);
            }
        }

        for(Map.Entry<Character, Integer> e: w1.entrySet()){
            int freq = e.getValue();
            if(f1.containsKey(freq)){
                f1.put(freq, f1.get(freq) + 1);
            }else{
                f1.put(freq, 1);
            }
        }

        for(char ch : word2.toCharArray()){
            if(w2.containsKey(ch)){
                w2.put(ch, w2.get(ch) + 1);
            }else{
                w2.put(ch, 1);
            }
        }

        for(Map.Entry<Character, Integer> e: w2.entrySet()){
            int freq = e.getValue();
            if(f2.containsKey(freq)){
                f2.put(freq, f2.get(freq) + 1);
            }else{
                f2.put(freq, 1);
            }
        }
        System.out.println(w1.keySet().toString());
        System.out.println(w2.keySet().toString());
        System.out.println(f1.values().toString());
        System.out.println(f2.values().toString());
        return w1.keySet().equals(w2.keySet()) && f1.equals(f2);
    }
}