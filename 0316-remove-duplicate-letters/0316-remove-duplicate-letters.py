class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = collections.Counter(s)
        stack = [] 
        c = set() 
        for i in s:
            table[i] -=1 
            while stack and stack[-1] > i and table[stack[-1]] >= 1 and i not in c :
                c.remove(stack.pop())
            if i not in c:
                stack.append(i)
                c.add(i)
        return ''.join(stack)