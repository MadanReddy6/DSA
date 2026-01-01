def stringPermutation(s1,s2):
    """
    Checks if a permutation of s1 is a substring of s2.

    Problem:
    Given two strings s1 and s2, return true if s2 contains a permutation of s1.

    Approach:
    - Iterate through s2 with a sliding window of size len(s1).
    - For each window, sort its characters and compare with sorted s1.
    - If they match, s1's permutation is found in s2.

    Time Complexity: O((N-M) * M log M)
    - N = len(s2), M = len(s1)
    - Sorting takes O(M log M).
    - We repeat this for (N - M + 1) windows.

    Space Complexity: O(M) for sorting.
    """
    
    for i in range(len(s2)-len(s1)+1):
        window = s2[i:i+len(s1)]
        if sorted(window) == sorted(s1):
            return True
            break
    return False

res=stringPermutation("ab","eidbaoo")
print(res)
        
# Optimal Solution

from collections import Counter

def stringPermutation(s1,s2):
    """
    Checks if a permutation of s1 is a substring of s2 using an optimal sliding window approach.

    Problem:
    Given two strings s1 and s2, return true if s2 contains a permutation of s1.

    Approach:
    - Use two frequency counters: one for s1 and one for the current window in s2.
    - Initialize the window counter with the first len(s1) characters of s2.
    - Slide the window one character at a time:
        - Add the new character to the window counter.
        - Remove the character going out of the window.
        - Compare the two counters.
    
    Time Complexity: O(N)
    - N = len(s2), M = len(s1)
    - Initial counter construction: O(M)
    - Sliding window loop: O(N)
    - Dictionary comparison: O(1) (since size is at most 26 for English alphabet)

    Space Complexity: O(1)
    - Counters store at most 26 characters.
    """
    
    k=len(s1)
    s1_counter=Counter(s1)
    window_counter=Counter(s2[:k])

    if s1_counter==window_counter:
        return True
    
    for i in range(k,len(s2)):
        window_counter[s2[i]]+=1
        window_counter[s2[i-k]]-=1
        if window_counter[s2[i-k]] == 0:
            del window_counter[s2[i-k]]

        if window_counter==s1_counter:
            return True
    return False
           

res=stringPermutation("ab","eidbaoo")
print(res)