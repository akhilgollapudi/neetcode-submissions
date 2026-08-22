class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        len_long_sub_str = 0
        maxi = 0
        start = 0
        seen = {}
        for ind in range(length):
            if s[ind] in seen:
                start = max(start, seen[s[ind]] +1)                    
            len_long_sub_str = ind-start + 1
            seen[s[ind]] = ind
            maxi = max(maxi, len_long_sub_str)

        return maxi