class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict={}
        for i in range(len(names)):
            my_dict[heights[i]]=names[i]
        sorted_dict=dict(sorted(my_dict.items() , key=lambda  item: item[0] , reverse=True))
       
        return list(sorted_dict.values())