class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        int n = nums.size();
         int p=0;
        for (int i = n - 1; i >= 2; i--) {
            if (nums[i-2] + nums[i-1] > nums[i]) {  
                p = nums[i] + nums[i-1] + nums[i-2];  
                return p;
            }
        }
        return 0; 
    }
};
