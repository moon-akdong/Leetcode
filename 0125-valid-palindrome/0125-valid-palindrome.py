class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 주어진 문자열이 팰린드롬인지 확인하라.
        # 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다
        new_s = re.sub('[^0-9a-zA-Z]','',s)
        array = []
        for i in new_s:
            array.append(i.lower())
        return array == array[::-1]
        