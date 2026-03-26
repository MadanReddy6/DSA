
# Brute force
def arrarProductExceptSelf(nums):
    n=len(nums)
    answer=[]
    
    for i in range(n):
        product =1
        for j in range(n):
            if i!=j:
                product*=nums[j]
        answer.append(product)
    return answer
l=[1,2,3,4]
print(arrarProductExceptSelf(l))



# Optimal solution

def productExceptSelf(nums):
    n=len(nums)
    answer=[1]*n
    
    prefix=1
    for i in range(n):
        answer[i]=prefix
        prefix*=nums[i]
        
    # suffix
    suffix=1
    for i in range(n-1,-1,-1):
        answer[i]*=suffix
        suffix*=nums[i]
        
    return answer

print(productExceptSelf(l))


