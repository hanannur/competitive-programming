class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        same_line=[]
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        
        for i in words:
            s=set(i.lower())
            if s.issubset(row1) or s.issubset(row2) or s.issubset(row3):
                same_line.append(i)
        return same_line




