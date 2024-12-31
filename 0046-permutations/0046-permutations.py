class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        prev = []
        def dfs(elements):
            if len(elements)==0:
                result.append(prev[:])
            for i in elements:
                next_elements = elements[:]
                next_elements.remove(i)

                prev.append(i)
                dfs(next_elements)
                prev.pop()
        dfs(nums[:])
        return result
