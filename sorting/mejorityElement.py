from collections import defaultdict 

def majorityElement(nums):
        count = defaultdict(int)
        n = len(nums)

        for num in nums:
            count[num] += 1
            if count[num] > n // 2:
                return num
res = majorityElement([3,2,3,2,2,2,2,2,2])          
print(res)

# moore's voting algorithm

def majorityElement(nums):
    count = 0
    candidate = 0
    
    for  num in nums:
        if count == 0:
            candidate = num
            count = 1
        if num == candidate:
            count += 1
        else:
            count -= 1
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return 'Majority element not exits' 
            
res = majorityElement([3,2,3,2,2,2,2,2,2])          
print(res)