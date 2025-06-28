class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sorted_list=[]
        sorted_list=[]

        for i in arr2:
            sorted_list.extend(arr1.count(i)*[i])
        visited=set()
        ar=[]
        for i in arr1:
            if i not in visited:
                visited.add(i)
                if i not in arr2:
                    ar.extend(arr1.count(i)*[i])
       
        sorted_list.extend(sorted(ar))
        return sorted_list
            
                

