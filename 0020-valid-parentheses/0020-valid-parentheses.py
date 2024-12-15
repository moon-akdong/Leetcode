class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s)<2:
            return False
        table = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        stack = [] 
        for char in s: 
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False 
                
        return True if not stack else False 