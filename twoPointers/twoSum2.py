# 167. Two Sum II - Input Array Is Sorted
# broute force approach
def twoSum(numbers, target):
    '''
    time complexity: O(n^2)
    space complexity: O(1)
    hits TLE on leetcode
    '''
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
        
        
        
# binary search approach
def twoSumBinary(numbers, target):
    '''
    time complexity: O(nlogn)
    space complexity: O(1)
    hits TLE on leetcode
    '''
    for i in range(len(numbers)):
        left = i + 1
        right = len(numbers)-1
        differ = target - numbers[i]
        
        while left <= right:
            mid = left + (right - left) // 2

            if numbers[mid] == differ:
                return [i + 1, mid + 1]
            elif numbers[mid] < differ:
                left += 1
            else:
                right -= 1
            
# optimal two pointer approach
def twoSumTwoPointer(nums, target):
    '''
    time complexity: O(n)
    space complexity: O(1)
    '''
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left+1 , right+1]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    
res=twoSumBinary([2,7,11,15],13)
print(res) #[1,3]


        