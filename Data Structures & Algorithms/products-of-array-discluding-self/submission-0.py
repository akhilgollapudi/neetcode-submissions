class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res =[0]*length
        for i,num in enumerate(nums):
            prod = 1
            for j,num in enumerate(nums):
                if i!=j :
                    prod *= num
            res[i] = prod
        return res
        
                