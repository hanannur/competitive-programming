class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start=0
        sqrt_value = c ** 0.5
        end = int(sqrt_value)
        #end=c//2

        while end>=start:
            if (start*start)+(end*end)==c:
                return True
            elif (start*start)+(end*end)<c:
                start+=1
               
            elif (start*start)+(end*end)>c:
                end -=1
        return False
        