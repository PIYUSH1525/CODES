from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]






nums = [3,3,4]
piyush =Solution()
print(piyush.majorityElement(nums))
