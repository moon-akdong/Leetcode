class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [] 
        prev = [] 

        def dfs(ls):
            # 리프 노드일 때 겨로가 추가 
            if len(ls) == 0:
                result.append(prev[:])
                return 
            
            for i in ls:
                next_ls = ls[:]
                next_ls.remove(i)
                prev.append(i)
                dfs(next_ls)
                prev.pop() # 백 트래킹? 
        dfs(nums)
        return result