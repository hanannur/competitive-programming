class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
       
        

        curr_sum = 0
        left = 0
        seen = set()
        max_sum = 0

        for i in range(len(nums)):
            
            while nums[i] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            
            seen.add(nums[i])
            curr_sum += nums[i]

            
            if i - left + 1 > k:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            
            if i - left + 1 == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum