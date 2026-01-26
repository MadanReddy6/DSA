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