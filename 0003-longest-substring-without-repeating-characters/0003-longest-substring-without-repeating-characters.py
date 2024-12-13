class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        
        start = max_len = 0 
        for idx ,char in enumerate(s):
            # 이미 있는 경우 
            if char in used and start <= used[char]:
                start = used[char] + 1 
                
            else:
                max_len = max(max_len,idx - start + 1)
                # 최대값 유지 
            used[char] = idx 
        return max_len

            
        