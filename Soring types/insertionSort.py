arr=[1, 9, 5, 3, 4, 2]


def insertionSort(nums):
    for i in range(1,len(nums)):
        curr=nums[i]
        previous=i-1
        
        while nums[previous]>curr and previous>=0:
            nums[previous+1]=nums[previous]
            previous-=1
        nums[previous+1]=curr
        
    return nums
        
res=insertionSort(arr)
print(res)