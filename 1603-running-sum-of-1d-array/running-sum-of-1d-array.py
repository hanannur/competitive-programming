class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum=[]
        left=0
        running_sum.append(nums[0])
        for i in range(1 ,len(nums)):
            added=running_sum[left]+nums[i]
            running_sum.append(added)
            left+=1
        return running_sum
