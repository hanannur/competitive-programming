class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if stack:
                if s[i] in {")","]","}"}:
                    if s[i] == ")" and stack[-1] == "(" or s[i] == "]" and stack[-1] == "[" or s[i] =="}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            
        print(stack)

        if not stack:
            return True
        else:
            return False

                    
                          