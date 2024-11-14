class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 주어진 문자열이 팰린드롬인지 확인하라.
        # 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다

        # 1. 대소문자 구분하지 않음 
        s = s.lower()
        
        # 2. 영문자와 숫자만을 대상으로 한다. 
        new_s = re.sub('[^0-9a-zA-Z]','',s)
        # array = []
        # for i in new_s:
        #   if i.isalnum()     
        #   array.append(i.lower())
        
        return new_s == new_s[::-1]
        # 알고리즘이라고 할만 한게 없다. / deque와 list사용법, 또는 슬라이싱 사용 
        # 대소문자 변경하는 방법과 정규표현식 정도