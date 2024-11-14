class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # 로그를 재정렬하라. 기준은 다음과 같다
        # 1. 로그의 가장 앞 부분은 식별자다.
        # 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
        # 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
        # 4. 숫자 로그는 입력 순서대로 한다.
        
        # 문자로 구성된 로그가 순사 로그보다 앞에 온다.
        letter,digits = [],[]
        for i in logs:
            if i.split()[1].isdigit():
                # 숫자 로그는 입력 순서대로 한다.
                digits.append(i)
            else:
                letter.append(i)
        # 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
        letter.sort(key =lambda x: (x.split()[1:],x.split()[0]))

        return letter + digits
        # 람다함수 사용법과 isditgit, sort 사용법 정도


