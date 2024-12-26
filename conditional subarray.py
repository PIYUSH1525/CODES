def count_valid_subarrays(N, X, A):
    left, right = 0, N - 1
    count = 0

    while left <= right:
        if A[left] + A[right] <= X:
            # All subarrays from A[left] to A[right] are valid
            count += (right - left + 1)
            left += 1  # Move the left pointer to the right
        else:
            right -= 1  # Decrease the right pointer to reduce the sum

    return count
