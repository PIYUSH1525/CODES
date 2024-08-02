class Solution:
    def two_sum(arr,target):
        one_pointer = 0
        two_pointer = len(arr) - 1
        while one_pointer < two_pointer:
            sum = arr[one_pointer] + arr[two_pointer]
            if sum == target:
                return(arr[one_pointer], arr[two_pointer])
            elif sum > target:
                one_pointer += 1
            else:
                two_pointer -= 1
arr = [1,2,3,4,5]
target = 7
alpha = Solution()
result = alpha.two_sum(arr, target)
print(result)