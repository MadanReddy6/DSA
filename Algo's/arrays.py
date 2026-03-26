
import array

a = array.array('f',[1.23,2.45,5.4856])

print(a)
# print(type(a))


arr1 = array.array('d', [3.1415926535, 2.718281828])
print(arr1)




# What is Precision?
# Precision refers to how many digits a number can have after the
# decimal point, and how accurately a number can be represented in memory.

balance = array.array('f', [123456789.123456789])
print(balance[0])  # Might show: 123456792.0 (wrong!)



balance = array.array('d', [123456789.123456789])
print(balance[0])  # Output: 123456789.12345679 (more accurate!)


marks = array.array('i',[62,98,75,34,56,78])

# print('accessing marks',marks[1])
# print('accessing marks',marks[2:3])
# print('accessing marks',marks[-1])

# looping by using for loop

for i, j in enumerate(marks):
    print('studnent number', i ,'and marks is' ,j )

# looping by using for and len,range

for i in range(len(marks)):
    print(marks[i])
print('---------')


# looping by using while loop
i=0
while i<len(marks):
    print(marks[i])
    i+=1
    
    
# loop for taking makrks input

# i=0
# marks=array.array('i',[])
# while i<5:
#     mark=int(input('enter studnet marks one by one'))
#     marks.append(mark)
#     i+=1

# print(marks)

marks = array.array('i',[62,98,75,34,-56,78,12])

def smallMarks(n):
    minMark=marks[0]
    for mark in marks:
        if mark < minMark:
            minMark=mark
    return minMark

# print('printing smallest marks',smallMarks(marks))



# Given an array of positive integers arr[] of size n, the task is to 
# find second largest distinct element in the array.

# Note: If the second largest element does not exist, return -1.


def secondHighest(n):
    fHighest=-1
    secondHighest=-1
    print(f'printing hight and second hight number{ fHighest,secondHighest}')
    for i in range(len(n)):
        if n[i]>fHighest:
            fHighest=n[i]
            
    for i in range(len(n)):
        if  n[i]>secondHighest and n[i]!=fHighest:
            secondHighest=n[i]
    return secondHighest


numbers=[1,2,3,4,5,6,8,9,7,8,9,1,2,5,50,40]
height=secondHighest(numbers)
# print('--height',height)



def secondLowest(n):
    firstLow=n[0]
    
    # loop for finding first low
    for i in range(len(n)):
        if n[i]<firstLow:
            firstLow=n[i]
            # print(firstLow)
            
    secondLow=n[0]
    # loop for finding second low
    for i in range(len(n)):
        if  n[i]<=secondLow and n[i]!=firstLow:
            secondLow=n[i]
    return secondLow


var=[1,3,45]
print("Second Lowest",secondLowest(var))


# finding nth highest 5

def nthHighest(n):
    rank=int(input('enter the which highest number you want to find:'))
    nthValue=0
    if rank<len(n):
        n.sort(reverse=True)
        print(f'sorted array{n}')
        nthValue=n[rank-1]
        print(nthValue)
    else:
        print('our of range error')
    return None
    


print(nthHighest([1,3,45,15,12,17,46]))
