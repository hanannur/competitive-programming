class Solution:
    def countTriples(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]
        sqrt_nums=[i**2 for i in range(1, n+1)]
        max_num=max(sqrt_nums)
        count=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                a=nums[i]*nums[i]
                b=nums[j]*nums[j]
                sum_=a+b
                if sum_>max_num:
                    break
                elif sum_ in sqrt_nums:
                    
                    count+=1
                # if sum_ in sqrt_nums:
                #     count+=1
        return count

        