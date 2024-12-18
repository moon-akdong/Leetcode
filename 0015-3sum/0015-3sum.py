class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [] 
        for ind in range(len(nums)-2):
            
            if ind != 0 and nums[ind-1] == nums[ind]:
                continue
            print(nums[ind],ind)
            left,right = ind +1, len(nums)-1
            while left < right:
                addNum = nums[ind] + nums[left] + nums[right]
                if addNum > 0 and right > left:
                    right -=1 
                elif addNum < 0 and left < right:
                    left +=1 
                
                else:
                    result.append([nums[ind],nums[left],nums[right]])   
                    c = 1
                    while left < right-c and nums[right-c] == nums[right]:
                        right -=1
                    c = 1 
                    while left+c < right and nums[left+c] == nums[left]:
                        left +=1 

                    right -=1 
                    left +=1 
        return result


        