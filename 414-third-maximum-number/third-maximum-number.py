class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))>=3:
            sets=list(set(nums))
            sorted_list=sorted(sets,reverse=True)
            return sorted_list[2]
        else:
            return max(nums)
