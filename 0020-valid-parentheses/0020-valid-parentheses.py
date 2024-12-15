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
            if char not in table: # table.keys() 하면 더 느려짐 
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False 

        return len(stack) == 0 
        # True if not stack else False 