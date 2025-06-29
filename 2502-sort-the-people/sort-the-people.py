class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair=[]
        for i in range(len(names)):
            pair.append((names[i],heights[i]))
        sorted_lst = sorted(pair, key=lambda x : x[1],reverse=True)
        final=[t[0] for t in sorted_lst]
        return final



