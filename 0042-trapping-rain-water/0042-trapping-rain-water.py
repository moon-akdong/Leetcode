class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = [] 
        water = 0 
        for i in range(len(height)): # distance 때문에 range(len(height))
        # 그리고 왠만한 상황 제외하고는 이렇게 시작하는게 좋은 듯 
            while stack and height[i] > height[stack[-1]]:
                pre = stack.pop() 
                if not stack: # 빼버리고 없으면 append를 위해 
                    break 
                distance = i - stack[-1] - 1
                # 같은 높이면 상쇄되서 volume = 0 이 됨 
                volume = min(height[stack[-1]],height[i]) - height[pre]
                water += distance * volume
            stack.append(i)
        return water

                
                

