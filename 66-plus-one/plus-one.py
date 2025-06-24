class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s=int(''.join(map(str,digits)))
        s+=1
        changed=[int(d) for d in str(s)]
        return changed