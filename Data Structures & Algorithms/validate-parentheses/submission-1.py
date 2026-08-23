class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in s:
            if i in pairs.values():
                stack.append(i)
            elif i in pairs.keys():
                if not stack:
                    return False
                top = stack[-1]
                if top == pairs[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False