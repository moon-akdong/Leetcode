class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 모든 경우의 수를 탐색 후 조합 
        def dfs(index,path):
            # digits 수량만큼의 문자길이를 가짐
            if len(path) == len(digits):
                result.append(path)
                return 
            # 입력값 자릿수 단위 반복
            for i in range(index,len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)
        
        if not digits:
            return [] 
        dic = {"2" : "abc",
                "3" : "def",
                "4":"ghi",
                "5":"jkl",
                "6":'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'}
        
        result = [] 
        dfs(0,"")
        return result