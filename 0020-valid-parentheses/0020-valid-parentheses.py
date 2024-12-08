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

            elif not stack or stack.pop() != map_table[i]:
                return False


        return False if stack else True 
        # return len(stack) == 0
        
