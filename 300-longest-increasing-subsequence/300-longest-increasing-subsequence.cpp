class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int maxLen = 0;
        vector<int> dp(nums.size(), 1);
        for(int i=0; i<nums.size(); i++){
           for(int j=i+1; j<nums.size(); j++){
               if(nums[i] < nums[j]){
                   dp[j] = max(dp[i]+1, dp[j]);
               }
           }
        }
        for(int num : dp){
            maxLen = max(maxLen, num);
        }
        return maxLen; 
    }
};