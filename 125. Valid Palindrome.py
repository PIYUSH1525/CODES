class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.replace("," , "")
        if s == s[::-1]:
            return True
        else:
            return False








s = "A man, a plan, a canal: Panama"
piyush = Solution()
print(piyush.isPalindrome(s))