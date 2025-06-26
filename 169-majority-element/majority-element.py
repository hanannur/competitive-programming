from collections import Counter 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
    

        maj=l//2
        for key,value in count.items():
            if value>maj:
                return key
        return 0