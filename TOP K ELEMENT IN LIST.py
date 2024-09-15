# Top K Elements in List
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
#
# The test cases are generated such that the answer is always unique.
#
# You may return the output in any order.
#
# Example 1:
#
# Input: nums = [1,2,2,3,3,3], k = 2
#
# # Output: [2,3]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = {}
        for i in nums:
            if i in hashset:
                hashset[i] += 1
            else:
                hashset[i] = 1
        sorted_elements = sorted(hashset.items(), key=lambda x: x[1], reverse=True)
        top_k = [item[0] for item in sorted_elements[:k]]

        return top_k

