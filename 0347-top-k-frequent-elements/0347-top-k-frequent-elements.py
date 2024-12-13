class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = collections.Counter(nums)
        freqs_heap = []
        result = [] 
        for f in freqs:
            heapq.heappush(freqs_heap,(-freqs[f],f))

        for _ in range(k):
            result.append(heapq.heappop(freqs_heap)[1])
        return result 
        