class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counted=[]
        for i in nums:
            count=0
            for j in range(len(nums)):
                if i>nums[j]:
                    count+=1
            counted.append(count)
        return counted

            
                