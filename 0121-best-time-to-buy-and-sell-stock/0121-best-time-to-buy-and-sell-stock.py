class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit = 0 
        # min_price = sys.maxsize
        # for price in prices:
        #     min_price = min(min_price,price)
        #     profit = max(profit,price-min_price)
        # return profit 

        price = 0 
        max_num = 0
        min_num = sys.maxsize
        for i in prices:
            max_num = max(i,max_num)
            min_num = min(i,min_num)
            if min_num == i:
                max_num = i 
            price = max(price,max_num - min_num) 
        return price


        