class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
       sorted_lst=sorted(score , key=lambda x : x[k] , reverse=True) 
       return sorted_lst   


                    
