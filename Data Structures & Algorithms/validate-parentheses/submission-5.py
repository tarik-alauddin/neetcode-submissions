class Solution:
    def isValid(self, s: str) -> bool:
        k = { "}": "{", "]": "[", ")": "("}
        stack = []

        for c in s:
            if c in k:
                if not stack or k[c] != stack.pop():
                    return False
            else:
                stack.append(c)
            
        if stack:
            return False
        return True
