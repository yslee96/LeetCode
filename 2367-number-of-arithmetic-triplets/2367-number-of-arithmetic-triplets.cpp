class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int res = 0;
        for(int i=0; i<nums.size(); i++){
            int first, second, third;
            first = nums[i];
            second = first + diff;
            third = second + diff;
            if(binary_search(nums.begin(), nums.end(), second) && binary_search(nums.begin(), nums.end(), third))
                res++;
        }
        return res;
    }
};