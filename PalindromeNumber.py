def ispalindrome(x):
    x=str(x)
    if x==x[::-1]:
        return True
    else:
        return False
    
print(ispalindrome(121))  # True
print(ispalindrome(-121)) # False
print(ispalindrome(10))   # False   