class Solution:
    def isPalindrome(self, x: int) -> bool:
        change=str(x)
        
        
        if change==change[::-1]:
            return True
        else:
            return False
