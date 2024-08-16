"Given an integer array nums, return true if any value appears at least twice in the array, and return"
"false if every element is distinct."
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (len(nums)):
            if nums[i] == nums[i+1]:
                return True
        return False









nums = [1, 2, 3, 1]
piyush = Solution.containsDuplicate(nums)