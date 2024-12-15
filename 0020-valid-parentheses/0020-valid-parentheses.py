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
            # 열린 bracket이 들어올 때 
            if char not in table: # table.keys() 하면 더 느려짐 
                stack.append(char)
            # 닫힌 Bracket이 들어왔을 때 
            # 해시맵 조회 및 비교 
            elif not stack or table[char] != stack.pop():
                return False 

        return len(stack) == 0 
        # 아래 주석이나 이거나 상관없음 단, 이게 조건이 뭔지 명확함
        # True if not stack else False 