class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left,right = 0,len(height)-1
        left_max,right_max = height[left],height[right]
        volume = 0 
        while left != right:
            # 1. 큰 쪽으로 이동 하도록 좌우 비교해서 이동 시킨다. (two point방법)
            # 2. 진행 중인 최대값을 유지하면서, 조회를 진행
            left_max,right_max = max(height[left],left_max), \
            max(height[right],right_max)
            # 3. 
            if left_max < right_max: 
                volume += left_max - height[left]
                left+=1 
            else:
                volume += right_max -height[right]
                right-=1 

        return volume