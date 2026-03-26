matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

# brute force 

def searchA2DMatrix(nums , target):
    
    for row in nums:
        for val in row:
            if val == target:
                return True
    return False
    

print(searchA2DMatrix(matrix , target))

# optimised binary search O(m*n)

def searchA2DMatrixBinary(matrix,target):
    
    row = len(matrix)
    column = len(matrix[0])

    left = 0
    right = row * column -1
    
    while left <= right:
        mid = left + (right - left) // 2
        midValue = matrix[mid // row] [mid % row]
        
        if midValue == target:
            return True
        elif midValue > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(searchA2DMatrixBinary(matrix , target))