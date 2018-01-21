"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ss in s:
            if ss in ['(', '[', '{']:
                stack.append(ss)
            else:
                if len(stack) == 0:
                    return False
                r = stack.pop()
                if ss == ')' and r != '(':
                    return False
                if ss == ']' and r != '[':
                    return False
                if ss == '}' and r != '{':
                    return False
        if len(stack) > 0:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isValid("([)]")
