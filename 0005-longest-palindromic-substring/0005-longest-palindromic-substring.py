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
                # right<=len(s) "="를 붙힌 이유는 출력단에서-1을 해주기 때문에 
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

# 투포인터로 풀었고, i+1,i+2 로 짝수홀수에 대응 했다. 
# max()함수에 key값으로 길이를 주어 길이가 가장 긴 것을 return 하게 했다.
