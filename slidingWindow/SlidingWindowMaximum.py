from collections import deque

def maxSlidingWindow(nums,k):
    """
    Finds the maximum value in each sliding window of size k.

    Problem:
    Given an array of integers nums and an integer k, return the max sliding window.

    Approach:
    - Use a Deque (Double Ended Queue) to store indices of array elements.
    - The deque will store indices in decreasing order of their corresponding values in nums.
    - Remove indices that are out of the current window (i - k).
    - Remove indices from the back whose values are smaller than the current element (maintain monotonic decreasing property).
    - The front of the deque always contains the index of the maximum element for the current window.

    Time Complexity: O(N)
    - N = length of the array
    - Each element is added and removed from the deque at most once.

    Space Complexity: O(k)
    - The deque stores at most k indices.
    """

    dq = deque()
    answer = []

    for i in range(len(nums)):

        # Remove out-of-window index
        if dq and dq[0] == i-k:
            dq.popleft()

        # Remove smaller values from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        # Add current index
        dq.append(i)
        
        # Add max to answer
        if i >= k-1:
            answer.append(nums[dq[0]])

    return answer

res = maxSlidingWindow([1,3,-1,-3,5,3,6,7] , 3)
print(res)