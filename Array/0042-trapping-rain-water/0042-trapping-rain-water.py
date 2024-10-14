class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointer solutions 
        if not height:
            return 0 
        water = 0 
        left,right = 0,len(height)-1 
        left_max,right_max = height[left],height[right]

        while left<right:
            left_max,right_max = max(height[left],left_max),\
                                max(height[right],right_max)
            if left_max <= right_max:
                print(left_max,height[left])
                water += left_max - height[left]
                print('water',water)
                left +=1 
            else:
                water += right_max - height[right]
                right -=1 
        return water


        # stack solutions
        # stack = [] 
        # water = 0 
        # for i in range(len(height)): # distance 때문에 range(len(height))
        # # 그리고 왠만한 상황 제외하고는 이렇게 시작하는게 좋은 듯 
        #     while stack and height[i] > height[stack[-1]]:
        #         pre = stack.pop() 
        #         if not stack: # 빼버리고 없으면 append를 위해 
        #             break 
        #         distance = i - stack[-1] - 1
        #         # 같은 높이면 상쇄되서 volume = 0 이 됨 
        #         volume = min(height[stack[-1],height[i]) - height[pre]
        #         water += distance * volume
        #     stack.append(i)
        # return water

        # stack => 이전 꺼와 비교하여 값을 더해주는 것 
        # two pointer => 진행하면서 더 작은 값이 나올 때 바로바로 더해주는 것 

