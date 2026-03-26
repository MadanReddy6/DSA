
arr=[1,1,2,2,3,3,4,5,5]

def singleElement(nums):
    for i in range(1,len(nums)-1):
        if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
            return i
        
res=singleElement(arr)
print(res)


