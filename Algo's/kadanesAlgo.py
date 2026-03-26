
# Brute Force:
# The term "brute force" refers to a straightforward approach to solving a problem by 
# trying every possible option and checking each one, without using any optimization or 
# clever algorithms. It's the most direct method, typically involving exhaustively 
# checking all possibilities.
 
# In your case, the brute-force approach to finding the maximum subarray sum involves the following:
# Generating all possible subarrays:
# You use two nested loops to generate every possible contiguous subarray of the list.
# Calculating the sum of each subarray:
# For each subarray, you calculate the sum of its elements.
# Comparing the sums:
# You keep track of the maximum sum as you check each subarray.



# lst=[3,-4,5,4,10,7,-8]
lst=[2, 3, -8, 7, -1, 2, 3]


def maxSubArray(n):
    res=n[0]
    maxsub=0
    for start in range(len(n)):
        for end in range(start,len(n)):
            subarry=n[start:end+1]
            temsum=sum(subarry)
            if temsum>res:
                res=temsum
                maxsub=subarry
                # return start,end
    return res , maxsub

# print(maxSubArray(lst))
    
# kadanes algo

# Using Kadane's Algorithm - O(n) Time and O(1) Space
# The idea of Kadane's algorithm is to traverse over the array from left to 
# right and for each element, find the maximum sum among all subarrays ending at that element. 
# The result will be the maximum of all these values. 

# But, the main issue is how to calculate maximum sum among all the subarrays ending 
# at an element in O(N) time?

# To calculate the maximum sum of subarray ending at current element, say maxEnding,
# we can use the maximum sum ending at the previous element. So for any element, 
# we have two choices:

# Choice 1: Extend the maximum sum subarray ending at the previous element by 
# adding the current element to it. If the maximum subarray sum ending at the previous 
# index is positive, then it is always better to extend the subarray.
# Choice 2: Start a new subarray starting from the current element. 
# If the maximum subarray sum ending at the previous index is negative, 
# it is always better to start a new subarray from the current element.
# This means that maxEnding at index i = max(maxEnding at index (i - 1) + arr[i], arr[i]) 
# and the maximum value of maxEnding at any index will be our answer. 

lst=[2, 3, -8, 7, -1, 2, 3]


def maxSubArry_kadanes(lst):
    res=lst[0]
    maxEnding=lst[0]
    subarr=0

    for i in range(1,len(lst)):
        
        maxEnding= max(maxEnding+lst[i],lst[i])
        res=max(res,maxEnding)
    return res

print(maxSubArry_kadanes(lst))

 