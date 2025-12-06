class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        left=1
        for i in range(len(nums)-1):
            left_sum=sum(nums[:left])
            right_sum=sum(nums[left:])
            sub_=left_sum-right_sum
            if sub_%2==0:
                count+=1
            left+=1
        return count

