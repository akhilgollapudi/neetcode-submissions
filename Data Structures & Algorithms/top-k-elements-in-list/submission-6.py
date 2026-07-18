from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        freq = {}
        for ind, val in enumerate(nums):
            freq[val] = 1 + freq.get(val,0)
        res = sorted(freq, key=lambda x: freq[x],reverse=True)
        return res[:k]
