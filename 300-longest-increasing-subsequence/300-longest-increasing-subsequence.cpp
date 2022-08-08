class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> seq;
        for(int i=0; i<nums.size(); i++){
            auto iter = lower_bound(seq.begin(), seq.end(), nums[i]);
            if(iter==seq.end()){
                //printf("it's okay to keep this seq\n");
                seq.push_back(nums[i]);
            }
            else{
                //printf("need to make a new seq\n");
                *iter = nums[i];
            }
        }
        return seq.size();
    }
};