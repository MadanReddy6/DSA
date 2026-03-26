arr=[4,1,5,2,3]

def selectionSort(nums):
    n=len(nums)
    for i in range(n):
        smallestIdx=i
        
        for j in range(i+1,n):
            if nums[j]<nums[smallestIdx]:
                smallestIdx=j
                
        nums[i],nums[smallestIdx]=nums[smallestIdx], nums[i]
        
    return nums

ans=selectionSort(arr)
print(ans)    