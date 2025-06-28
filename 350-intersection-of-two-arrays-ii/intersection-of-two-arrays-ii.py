class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=[]
        int_cp1=nums1.copy()
        int_cp2=nums2.copy()
        for i in nums1:
            if i in int_cp2:
                intersection.append(i)
                int_cp1.remove(i)
                int_cp2.remove(i)

        return intersection 