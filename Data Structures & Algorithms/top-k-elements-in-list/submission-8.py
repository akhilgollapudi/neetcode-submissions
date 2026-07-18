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
        """

        max_len = len(nums)
        bucket = [[] for _ in range(max_len + 1) ]
        freq = {}
        for ind, val in enumerate(nums):
            freq[val] = 1 + freq.get(val,0)
        for num, count in freq.items():
            bucket[count].append(num)
        ans = []
        for i in range(max_len, -1, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        print(ans)

