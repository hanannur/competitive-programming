class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
       
        count=0
        sorted_lst=sorted(people)
        left=0
        right=len(people)-1
    
        


        while right>=left:
            if sorted_lst[right]+sorted_lst[left]<=limit:
                left+=1

            right-=1
            count+=1

          


        return count






        #[1,2,2,3] limit=5



        