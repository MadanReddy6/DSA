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