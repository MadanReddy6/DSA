
# Moore’s Voting Algorithm is used to find the majority element in an array — 
# an element that appears more than n / 2 times.

# 🔁 Moore’s Voting Algorithm Logic:
# Initialize:

# A count variable = 0

# A candidate variable = None

# Iterate through the array:

# If count is 0, set candidate = current element

# If current element == candidate, increment count

# Else, decrement count

# After one pass, candidate will hold the majority element.


def majorityElement(n):
    candidate=0
    count=0
    
    for i in n:
        if count==0:
            candidate=i
            count=1
        elif i==candidate:
                count+=1
        else:
            count-=1
            
    if n.count(candidate) > len(n)//2:
        return candidate
    else:
        return 'no mejority element found'
        
            


nums = [2, 2, 1, 1, 2, 2]
# nums = [1, 2, 3, 4]

print(majorityElement(nums))
