class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        right_product = 1
        n = len(nums)
        result = [1] * len(nums)
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        for i in range( n-1,-1,-1):
            result[i] = result[i]*right_product
            right_product *= nums[i]
        return result
