from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        freq = {}
        for ind, val in enumerate(nums):
            freq[val] = 1 + freq.get(val,0)
        res = sorted(freq, key=lambda x: freq[x],reverse=True)
        return res[:k]
        """
        heap = []
        freq = {}
        for ind, val in enumerate(nums):
            freq[val] = 1 + freq.get(val,0)
        for num, count in freq.items():
            # push (count, num)
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
                # pop
        res = []
        res =  [num for count, num in heap]
        print(heap)
        return res
        # extract only the numbers