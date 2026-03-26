
# maxWater=0

# for i in range(len(height)):
#     for j in range(i+1,len(height)):
#         width=j-i
#         height_=min(height[i],height[j])
#         curretWater=width*height_
#         maxWater=max(curretWater,maxWater)
            
# print(maxWater)

height=[1,8,6,2,5,4,8,3,7]
def maxArea(n):
    left=0
    right=len(n)-1
    maxWater=0
    while left<right:
        width=right-left
        h=min(n[left],n[right])
        
        area=width*h
        maxWater=max(maxWater,area)
        
        if n[left] < n[right]:
            left+=1
        else:
            right-=1
    return maxWater
        
        
# water=maxArea(height)
# print(water)





nums = [1, 2, 3, 4]
n=len(nums)
for i in range(n,-1,-1):
    print(i)