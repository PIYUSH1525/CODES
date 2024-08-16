from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # APPROACH 2
        "Using Dictionary Key value pair"
        # l = len(nums)
        # dicto = {}
        # for num in nums:
        #     if num not in dicto:
        #         dicto[num] = 1
        #     else:
        #         dicto[num] += 1
        #     if dicto[num] > l // 2:
        #         return num


        # APPROACH 1
        "the majority element will always come in center due to the condition n/2 so sort the array and return"
        "the center element "
        # nums.sort()
        # return nums[len(nums)//2]










nums = [3,3,4]
piyush =Solution()
print(piyush.majorityElement(nums))
