def max_sum_subarray(arr):
    """
    Calculates the maximum sum of a contiguous subarray in an array using Kadane's algorithm.

    Args:
        arr (list): Input array of integers.

    Returns:
        int: Maximum sum of a contiguous subarray.
    """
    if not arr:
        return 0  # Empty array, return 0

    max_sum = arr[0]  # Initialize max_sum with the first element of the array
    # Initialize current_sum with the first element of the array
    current_sum = arr[0]

    for num in arr[1:]:
        # Update current_sum as the maximum of current element and the sum of current_sum and current element
        current_sum = max(num, current_sum + num)
        # Update max_sum as the maximum of max_sum and current_sum
        max_sum = max(max_sum, current_sum)

    return max_sum
