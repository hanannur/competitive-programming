class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        inboth=[]
        num4=list(set(nums1))
        num5=list(set(nums2))
        num6=list(set(nums3))
        for i in range(len(num4)):
            if num4[i] in num5 or  num4[i] in num6:
                inboth.append(num4[i])
        for i in range(len(num5)):
            if num5[i] in num4 or num5[i] in num6:
                inboth.append(num5[i])
        for i in range(len(num6)):
            if num6[i] in num4 or  num6[i] in num5:
                inboth.append(num6[i])
        return list(set(inboth))

            