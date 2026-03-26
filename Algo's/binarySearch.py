
# Binary Search Algorithm is a searching algorithm used in a sorted array by 
# repeatedly dividing the search interval in half. 
# The idea of binary search is to use the information that the array is sorted and 
# reduce the time complexity to O(log N). 

# Below is the step-by-step algorithm for Binary Search:

# Divide the search space into two halves by finding the middle index “mid”. 
# Compare the middle element of the search space with the key. 
# If the key is found at middle element, the process is terminated.
# If the key is not found at middle element, choose which half will be used as the next search space.
# If the key is smaller than the middle element, then the left side is used for next search.
# If the key is larger than the middle element, then the right side is used for next search.
# This process is continued until the key is found or the total search space is exhausted.

l=[-1,0,3,4,8,9,10,12]
target=12

def binarySearch(n,target):
    st=0
    end=len(n)-1
    
    while st <= end:
        mid=(st+end)//2
        if target>n[mid]:
            st=mid+1
        elif target<n[mid]:
            end=mid-1
        else:
            return mid
        
    return -1
                
# result=binarySearch(l,target)
# print(result)

# rotated sorted array
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
def rotatedSortedArray(nums,target) -> int:
    st=0
    end=len(nums)-1
    while st<=end:
        mid=(st+end)//2
        
        if nums[mid]==target:
            return mid
        
        if nums[st]<=nums[mid]:
            if nums[st]<=target<nums[mid]:
                end=mid-1
            else:
                st=mid+1

        else:
            if nums[mid]<target<=nums[end]:
                st=mid+1
            else:
                end=mid-1
            
    return -1

result=rotatedSortedArray(nums,target)
print(result)