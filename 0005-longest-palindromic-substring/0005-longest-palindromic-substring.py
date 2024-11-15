class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 중앙을 찾을 필요가 없다. -> 문장 내 팰리드롬이 있는지를 찾는 것 "abb"이런 예제가 있음 
        # 투포인터 
        def expand(left,right):
            while left>=0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1] # while 문으로 늘렸다가 아니면 이전꺼로 돌아가야 하므로

        if len(s) <2 or s == s[::-1]:
            return s
        result = ""
        for i in range(len(s)-1):
            result = max(result,
                            expand(i,i+1),
                            expand(i,i+2),
                            key=len)
        return result