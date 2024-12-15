class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 예외조건 
        if len(nums) == 2:
            return [0,1]

        # 탐색을 위한 해쉬맵 만들기, index 찾아주는 함수 
        # table = {}
        # for num in enumerate(nums):
        #     table[num] = target - num
             
        for idx in range(len(nums)):
            # 조건1 
            t = target - nums[idx]
            if t in nums and nums.index(t) != idx:
                return [idx,nums.index(t)]