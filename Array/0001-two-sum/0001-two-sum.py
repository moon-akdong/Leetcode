class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two-pointer는 안됨
        if len(nums) < 2:
            return nums
        # dict
        table = dict()
        for ind,val in enumerate(nums):
            table[val] = ind
        
        for ind,val in enumerate(nums):
            if target-val in table and ind != table[target-val]:
                return [ind,table[target-val]]