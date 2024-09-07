def min_operations_to_palindrome(data):
    n = len(data)
    left, right = 0, n - 1
    operations = 0

    while left < right:
        if data[left] != data[right]:
            if data[left] < data[right]:
                data[left:right + 1] = data[left:right + 1][::-1]
            else:
                data[left:right + 1] = data[left:right + 1][::-1]
            operations += 1
            left, right = 0, n - 1
            continue
        left += 1
        right -= 1

    return operations

data = [3, 5, 2, 5, 7]
print("Minimum operations to make array palindromic:", min_operations_to_palindrome(data))
print("Transformed array:", data)
