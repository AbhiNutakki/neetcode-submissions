class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        possibleoptions = {')':'(','}':'{',']':'['}
        for i in s:
            if i in possibleoptions:
                if stack and stack[-1] == possibleoptions[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

