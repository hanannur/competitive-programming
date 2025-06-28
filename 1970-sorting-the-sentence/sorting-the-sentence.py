class Solution:
    def sortSentence(self, s: str) -> str:
        s_p=s.split()
        sorted_lst=sorted(s_p,key=lambda x: x[-1])
        corrected=[i[:-1] for i in sorted_lst]
        final=' '.join(corrected)
        return final

