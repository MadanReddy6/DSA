arr=[1, 9, 5, 3, 4, 2]

def bubleSort(nums):
    n=len(nums)
    
    for i in range(n-1):
        for j in range(n -1 -i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                isSwap=True
                
        
    return nums


# optimized bubble sort
def bubbleSort(nums):
    n = len(nums)
    for i in range(n - 1):
        isSwap = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                isSwap = True
    if not isSwap:
        print("Array is already sorted.")
        
    return nums


ans=bubbleSort(arr)
print(ans)



