class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out  = []
        # left 
        p = 1 
        for i in range(len(nums)):
            out.append(p)
            p = p *nums[i]
        # left result 와 right 값 곱셈
        p = 1
        for i in range(len(nums)-1,-1,-1):
            out[i] = out[i]*p
            p = p *nums[i]
        return out 
        # 결론 : 아직 부족하다. 실제 머리 속에 있는 것을 구현하는 능력이 떨어진다.
        # 너무 단순하게 풀고 있는 있는 듯한 느낌 
        
        # p1,p2,p3= [],[],[]
        # s =1 
        # for i in nums[:-1]:
        #     p1.append(s)
        #     s = i * s
            
        # s = 1 
        # re_nums = nums[::-1]
        # for j in re_nums[:-1]:
        #     p2.append(s)
        #     s = s * j
            
        # print(p1,p2)
        # p2 = p2[::-1]
        # for ind in range(len(p1)):
        #     p3.append(p1[ind]*p2[ind])
        # return p3
