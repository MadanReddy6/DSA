# Leetcode 647

def palindromeSubstring(s):
    
    answer = 0
    length = len(s)
    
    def checkPalindrome(l , r):
        nonlocal answer
        
        while l >= 0 and r < length and s[l] == s[r]:
            l -= 1
            r += 1
            answer += 1
        
            
    for i in range(length):
        checkPalindrome(i , i) #odd palindrome
        checkPalindrome(i , i + 1) #even palindrome
        
    return answer

print(palindromeSubstring('abc'))