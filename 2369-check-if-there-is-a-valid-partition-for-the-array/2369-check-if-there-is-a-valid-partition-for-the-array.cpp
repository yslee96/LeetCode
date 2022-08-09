class Solution {
public:
    bool validPartition(vector<int>& nums) {
        bool dp[100001] = {false, };
        if(nums[0]==nums[1])
            dp[1] = true;
        if(nums.size()>2){
            if(nums[2]==nums[1] && nums[1]==nums[0]){
                dp[2] = true;
            }
            if(nums[2]-2 == nums[1]-1 && nums[1]-1 == nums[0]){
                dp[2] = true;
            }
        }
        for(int i=3; i<nums.size(); i++){
            if(dp[i-2]){
                if(nums[i] == nums[i-1]){
                    dp[i] = true;
                }
            }
            if(dp[i-3]){
                if(nums[i]==nums[i-1] && nums[i-1] == nums[i-2]){
                    dp[i] = true;
                }
                if(nums[i]-2==nums[i-1]-1 && nums[i-1]-1==nums[i-2]){
                    dp[i] = true;
                }
            }
        }
        return dp[nums.size()-1];
    }
};