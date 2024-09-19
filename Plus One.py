from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1
        while index >= 0:
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] = digits[index]+1
                return digits
            index = index-1
        return [1] + digits



gvbfdgvbdf
dzxfc





digits = [9,9,9]
alpha = Solution()
result = alpha.plusOne(digits)
print(result)
# Output: [1,2,4]