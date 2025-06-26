class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_list=sorted(score,reverse=True)
        rank=[]
        first="Gold Medal"
        second="Silver Medal"
        third="Bronze Medal"
        for i in range(len(score)):
            if score[i]==max(score):
                rank.append(first)
            elif score[i]==sorted_list[1]:
                rank.append(second)
            elif score[i]==sorted_list[2]:
                rank.append(third)
            else:
                rank.append(str(sorted_list.index(score[i])+1))
        return rank