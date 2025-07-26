class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sums=[]
        left=0
        while left<len(nums):
            sums.append(nums[left])
            left+=2
        return sum(sums)