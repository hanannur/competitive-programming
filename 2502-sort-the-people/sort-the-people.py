class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_names=[(names[i] ,heights[i]) for i in range(len(names))]
        sortd_name = sorted(sorted_names , key=lambda x : x[1], reverse=True)
        final=[]
        for i in range(len(names)):
            final.append(sortd_name[i][0])
        return final

        