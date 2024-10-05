class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [0] * len(temperatures)
        ind_list = [] 
        for ind,cur in enumerate(temperatures):
            while ind_list and temperatures[ind_list[-1]] < cur:
                last = ind_list.pop()
                stack[last] = ind - last
            ind_list.append(ind)
        return stack