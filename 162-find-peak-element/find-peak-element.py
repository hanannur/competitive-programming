class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num=max(nums)
        return(nums.index(max_num))