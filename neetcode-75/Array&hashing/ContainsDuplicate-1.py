
def containDuplicate(nums):
    Seen = set()
    
    for num in nums:
        if num in Seen:
            return True
        Seen.add(num)
    return False

print(containDuplicate([1, 2, 3])) #Flase
print(containDuplicate([1, 2, 3, 3])) #True

        