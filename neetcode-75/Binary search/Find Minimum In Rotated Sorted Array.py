
# def findMinInRotatedSortedArray(nums):
#     return min(nums)





def findMinInRotatedSortedArray(nums):
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] < nums[right]:
            return nums[left]
        
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
             
    return nums[left]
    

print(findMinInRotatedSortedArray([3,4,5,6,-9,0,1,2]))

