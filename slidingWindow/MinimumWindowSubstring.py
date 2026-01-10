
from collections import Counter , defaultdict

def minWindowSubstring(s,t):
    """
    Finds the minimum window substring in s that contains all characters of t.

    Problem:
    Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

    Approach:
    - Use two pointers (left and right) to create a sliding window.
    - Use a hash map (Counter) to store the frequency of characters in t (need).
    - Use another hash map to store the frequency of characters in the current window.
    - Expand the window by moving the right pointer until it contains all characters of t.
    - Once valid, shrink the window from the left to minimize its size while maintaining validity.
    - Track the minimum window size and its starting/ending indices.

    Time Complexity: O(N)
    - N = length of string s.
    - Each character in s is visited at most twice (once by right pointer, once by left pointer).

    Space Complexity: O(K)
    - K = size of the character set (or unique characters in t).
    - We store counts for characters in t and the current window.
    """
    if not s or not t:
            return ""

    need = Counter(t)
    window = defaultdict(int)

    have = 0
    need_count = len(need)

    res = [-1, -1]
    res_len = float("inf")

    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] += 1

        if char in need and window[char] == need[char]:
            have += 1

        # Try to shrink window
        while have == need_count:
            # Update result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # Remove left character
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1

            left += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""


res = minWindowSubstring("ADOBECODEBANC","ABC")
print(res)
