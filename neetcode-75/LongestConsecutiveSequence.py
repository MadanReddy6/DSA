

def LongestConsecutiveSequence(nums):
    
    numSet = set(nums)
    Longest = 0
    
    for num in nums:
        # check num is start of sequence
        if num - 1 not in numSet:
            current = num
            lenght = 1
            while current + 1 in numSet:
                current += 1
                lenght += 1
            Longest = max(Longest , lenght)
    return Longest

print(LongestConsecutiveSequence([2,6,20,4,7,10,3,4,5]))