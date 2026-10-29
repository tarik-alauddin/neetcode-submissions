class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) != 0 and closeToOpen[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if len(stack) != 0:
            return False
        return True
            
                