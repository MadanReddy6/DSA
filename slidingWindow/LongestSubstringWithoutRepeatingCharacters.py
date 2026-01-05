def lengthOfLongestSubstring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Problem:
    Given a string s, return the length of the longest substring without repeating characters.

    Approach:
    - Use a sliding window with two pointers (left and right).
    - Use a set to track unique characters in the current window.
    - Expand the window by moving the right pointer and add characters to the set.
    - If a duplicate character is found, shrink the window from the left until the duplicate is removed.
    - Keep track of the maximum window size.

    Time Complexity: O(N)
    - N = length of the string
    - Each character is processed at most twice (once by right pointer, once by left pointer).

    Space Complexity: O(min(N, M))
    - M = size of the character set (e.g., 26 for English alphabet)
    - Set stores unique characters in the current window.
    """
    
    left = 0
    answer =0
    seen = set()
    
    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        answer = max(answer,right-left+1)
    return answer   

res=lengthOfLongestSubstring("abcdeabcbb")
print(res)