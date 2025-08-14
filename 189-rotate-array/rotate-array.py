class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:]=nums[::-1]
        k = k % len(nums)
        right=k-1
        left=0
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        
        right=len(nums)-1
        left=k
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

