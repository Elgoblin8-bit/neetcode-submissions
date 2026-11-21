class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            if not stack:
                return False
            
            if char == ')':
                if '(' != stack.pop():
                    return False
            elif char == '}':
                if '{' != stack.pop():
                    return False
            elif char == ']':
                if '[' != stack.pop():
                    return False
        if stack:
            return False
        return True


        