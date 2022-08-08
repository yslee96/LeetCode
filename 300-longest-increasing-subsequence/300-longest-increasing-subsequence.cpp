class Solution {
public:
    int dp[2501];
    int maxLen = 1;
    int lengthOfLIS(vector<int>& nums) {
       for(int i=0; i<nums.size(); i++)
            dp[i] = 1;
       
        for(int i=1; i<nums.size(); i++){
           for(int j=0; j<i; j++){
               if(nums[i] > nums[j] && dp[i] < dp[j]+1){
                   dp[i] = dp[j]+1;
               }
           }
           maxLen = max(dp[i], maxLen);
       }
       return maxLen; 
    }
};