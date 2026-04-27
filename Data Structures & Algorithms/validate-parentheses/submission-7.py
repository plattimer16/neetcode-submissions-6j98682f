class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        opened = ['(', '[', '{']
        for brace in s:
            if brace in opened:
                stack.append(brace)
            elif not stack:
                return False
            else:
                last = stack.pop()
                if brace == ']' and last != '[':
                    return False
                elif brace == '}' and last != '{':
                    return False
                elif brace == ')' and last != '(':
                    return False
        if stack:
            return False
        return True