from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # APPROACH 3
        "USING VOTING ALGO"
        Vote = 1
        majority_element = nums[0]
        for i in range(1,len(nums)):
            if Vote == 0:
                majority_element = nums[i]
                Vote += 1
            elif majority_element == nums[i]:
                Vote +=1
            else:
                Vote -=1
        return majority_element





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


nums = [3,4,3,4,3]
piyush =Solution()
print(piyush.majorityElement(nums))
