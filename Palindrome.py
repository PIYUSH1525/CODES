class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        n = z[::-1]
        if n == z:
            return True
        else:
            return False

x = -111
solution = Solution()
print(solution.isPalindrome(x))