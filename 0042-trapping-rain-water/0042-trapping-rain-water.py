class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volume = 0 
        r = 0 
        stack = [] 
        while r < len(height):
            while stack and height[r] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance  = r-stack[-1] -1 
                waters = min(height[r],height[stack[-1]])-height[top]
                volume += distance * waters
            stack.append(r)
            r += 1 
        return volume 


            