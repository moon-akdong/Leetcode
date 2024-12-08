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
        for i in s: 
            if i not in map_table.keys():
                stack.append(i)

            elif (i in map_table.keys() and not stack) or stack.pop() != map_table[i]:
                return False

        if not stack:
            return True 
        return False 
        
