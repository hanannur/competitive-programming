class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sorted_lst=sorted(skill)
        if len(skill)%2 !=0:
            return -1
        left=0
        right=len(skill)-1
        check=sorted_lst[left]+sorted_lst[right]
        total=0
        while right>left:
            current_sum=sorted_lst[left]+sorted_lst[right]
            if current_sum!=check:
                return -1
            total+=sorted_lst[left]*sorted_lst[right]
            left+=1
            right-=1
        return total
        