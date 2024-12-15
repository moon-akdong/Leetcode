class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s)<2:
            return False
        map_table = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        stack = [] 
        for char in s: 
            if char in map_table.keys():

                if not stack or stack.pop() != map_table[char]:
                    return False 
            else:
                stack.append(char)
        return True if not stack else False 