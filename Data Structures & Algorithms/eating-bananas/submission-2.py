class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        1 hour - 1 in 2 hrs
        2nd hour - 4 - 2 hr rem 2 - 5th 2-2 
        3rd hour - 3 - 2 hr rem 1 - 6th 1-2
        4th hour - 2- 2 hr r
        """

        left = 1
        right = max(piles)
    
        while left < right:
            mid = (left + right) // 2
            hours_needed = 0
            for pile in piles:
                hours_needed += (pile + mid - 1)//mid
            if hours_needed <= h:
                right = mid
            else:
                left = mid + 1
        return left
