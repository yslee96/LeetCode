class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> occurMap = new HashMap<>();
        Set<Integer> freqSet = new HashSet<>();
        for(int num : arr){
            if(occurMap.containsKey(num)){
                occurMap.put(num, occurMap.get(num)+1);
            }else{
                occurMap.put(num, 1);
            }
        }

        int [] freqs = new int [1000];
        for(Map.Entry<Integer, Integer> e : occurMap.entrySet()){
            int freqNum = e.getValue();
            if(freqSet.contains(freqNum)){
                return false;
            }else{
                freqSet.add(freqNum);
            }
        }
        return true;
    }
}