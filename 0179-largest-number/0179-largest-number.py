class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(x) for x in nums]

        nums.sort(key=lambda x: x * 10, reverse=True)

        ans = "".join(nums)

        if ans[0] == "0":
            return "0"

        return ans