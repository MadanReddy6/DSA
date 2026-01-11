# 167. Two Sum II - Input Array Is Sorted

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
        
        
res=twoSum([2,7,11,15],17)
print(res)


        