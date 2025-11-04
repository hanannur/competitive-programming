class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        phase_sum=sum(nums[:k])
        sub_array=[phase_sum]      
        for i in range(len(nums)-k):
            phase_sum+=(nums[k+i]-nums[i])
            sub_array.append(phase_sum)

        return max(sub_array)/k

