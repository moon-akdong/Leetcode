class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        freqs = {}
        count =0 

        # 해시맵으로 만든다. 
        # collections.Counter(stones)
        for char in stones:
            if char not in freqs:
                freqs[char] = 1 
            else:
                freqs[char] +=1 
        
        for char in jewels:
            if char in freqs:
                count += freqs[char]
        return count 
        