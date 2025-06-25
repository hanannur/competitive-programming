class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=[]
        for i in range(len(nums)):
            s=nums.count(nums[i])
            count.append(s)
        for i in range(len(count)):
            if count[i]==1:
                not_repeated=nums[i]
        return (not_repeated)