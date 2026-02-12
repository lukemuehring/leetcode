class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {'}':'{',']':'[',')':'('}

        for c in s:
            if c in matches:
                if len(stack) > 0 and stack[-1] == matches[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) > 0:
            return False
        else:
            return True




        