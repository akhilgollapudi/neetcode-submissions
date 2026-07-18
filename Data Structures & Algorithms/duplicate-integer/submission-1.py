class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for ind, num in enumerate(nums):
            if num in seen:
                return True
            seen[num] = ind
        return False