class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping:  # If it's a closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False  # Invalid character

        return not stack  # True if stack is empty
