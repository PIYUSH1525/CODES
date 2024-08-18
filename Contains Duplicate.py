"Given an integer array nums, return true if any value appears at least twice in the array, and return"
"false if every element is distinct."
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        "APPROACH 2 USING HASH SET`"
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


        "APPROACH 1"

        # nums.sort()
        # for i in range (len(nums)):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        #







nums = [2, 14, 18, 22, 22]  # List to check for duplicates
piyush = Solution()
print(piyush.containsDuplicate(nums))