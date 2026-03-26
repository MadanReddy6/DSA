# leetcode 153

arr = [5,6,3,4]

def findMin(arr):
    """
    Finds the minimum element in a rotated sorted array using a brute-force linear scan.

    Args:
        arr (list): The input list of numbers, which is a rotated sorted array.

    Returns:
        int: The minimum element in the array.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    answer = arr[0]
    for i in range(len(arr)):
        if arr[i] < answer:
            answer = arr[i]
    return answer

def findMinOptimal(arr):
    """
    Finds the minimum element in a rotated sorted array using binary search.

    Args:
        arr (list): The input list of numbers, which is a rotated sorted array.
                    Assumes distinct elements.

    Returns:
        int: The minimum element in the array.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]

print("Brute-force min:", findMin(arr))
print("Optimal min:", findMinOptimal(arr))
