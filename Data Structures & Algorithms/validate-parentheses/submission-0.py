class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeandopen = {")":"(","}":"{","]":"["}
        for i in s:
            if i in closeandopen:
                if stack and stack[-1] == closeandopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

