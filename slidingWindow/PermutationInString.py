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

res=stringPermutation("ab","eidboaoo")
print(res)
        
