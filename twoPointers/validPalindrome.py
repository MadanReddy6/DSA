# Brute Force Approach
import inspect


def isPalindrome1(s):
    """
    Brute-force check whether `s` is a palindrome.

    This function builds a cleaned, lowercase-only-alphanumeric copy of
    the input and compares it to its reverse.

    Time complexity: O(n) — one pass to build `cleaned_string` and another
    for the reverse/comparison.
    Space complexity: O(n) — stores `cleaned_string` (up to length n).

    Parameters:
    - s (str): Input string to check.

    Returns:
    - bool: `True` if `s` is a palindrome (ignoring non-alphanumerics and case),
      otherwise `False`.
    """
    cleaned_string = ''.join( c.lower() for c in s if c.isalnum())
    if cleaned_string == cleaned_string[::-1]:
        return True
    return False

# Optimal Two Pointer Approach
def isPalindrome(s):
    """
    Two-pointer check whether `s` is a palindrome.

    This implementation uses two indices scanning inward from both ends,
    skipping non-alphanumeric characters and comparing characters case-insensitively.

    Time complexity: O(n) — each character is visited at most once by either pointer.
    Space complexity: O(1) — only a few integer pointers are used.

    Parameters:
    - s (str): Input string to check.

    Returns:
    - bool: `True` if `s` is a palindrome (ignoring non-alphanumerics and case),
      otherwise `False`.
    """
    l = 0
    r = len(s)-1
    
    while l<r:
        while l<r and not s[l].isalnum():
            l+=1
        while l<r and not s[r].isalnum():
            r-=1
        if s[l].lower() != s[r].lower():
            return False

        l+=1
        r-=1
    return True

print(inspect.getdoc(isPalindrome))


# res = isPalindrome('A man, a plan, a canal: Panama')
# print(res) #True