
def LongestSubstringWithoutRepeatingCharacters(s):
    
    res = 0
    
    left = 0
    seen = set()
    
    for right in range(len(s)):
        if s[right] in seen:
            left += 1
            
        seen.add(s[right])
        res = max(res , right - left +1)
        
    return res

print(LongestSubstringWithoutRepeatingCharacters("zxyzxyz"))