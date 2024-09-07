# Palindromic sequences are employed as test cases to evaluate the performance of a machine-learning algorithm designed
# for detecting and manipulating palindromic patterns. Given an array of integers data of size n, the objective is to
# convert the array into a palindromic sequence for testing the ML algorithm.
# 1
# The available operation for manipulating the array is as follows:
# • Choose two integers xand y.
# • Replace every occurrence of x in the array with y.
# The task, of using this operation as a data preprocessing technique, is to determine the minimum number of such
# operations required to transform the array data into a palindrome.
# Note that An array is considered palindromic if it remains the same when its elements are reversed, that is
# arrfif = arrn - 1 - il, where 0 ≤ i < n, for an array arr of size n.
# Example
# 7=6
# data = [1, 2, 3, 3, 1, 4]
# approach 2 is to swap the whole list when left and right are not same
def min_operations_to_palindrome(data):
    n = len(data)
    left, right = 0, n - 1
    operations = 0
    mid = len(data)//2
    while left < right:
        if data[left] != data[right]:
            if data[left] < data[right]:
                data[left:right + 1] = data[left:right + 1][::-1]
            else:
                data[left:right + 1] = data[left:right + 1][::-1]
            operations += 1
        left, right = 0, n - 1
    data[mid]= data[mid+1]
    return operations

data = [3, 5, 2, 5, 3]
print("Minimum operations to make array palindromic:", min_operations_to_palindrome(data))
print("Transformed array:", data)

