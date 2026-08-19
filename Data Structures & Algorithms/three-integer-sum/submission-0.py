class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        left=0
        length = len(nums) -1
        for i in range(length):
            left=i+1
            right = length
            if i > 0 and nums[i] == nums[i-1]:
               continue
             
            while left < right: 
                sum = nums[left] + nums[right]
                if sum < -nums[i]:
                    left+=1
                elif sum > -nums[i]:
                    right -= 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)
                    left+=1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while right>left and  nums[right] == nums[right+1]:
                        right -=1
        return result

