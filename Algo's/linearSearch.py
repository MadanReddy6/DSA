import array

# Linear search by using for loop

# marks = array.array('i',[62,98,75,34,-56,78,12])

# target=12
      
# found = False

# for i in range(len(marks)):
#     if marks[i] == target:
#         print(i)
#         print('found target at index ',i)
#         found = True
#         break
    
# if found==False:
#     print('did not fund the target')


def linearSearch(lst,tar):
    for i in range(len(lst)):
        if lst[i]==tar:
           return i
    return -1


marks = array.array('i',[24,45,78,64,78,96])
target=78

find_target=linearSearch(marks,target) 
print(find_target)
if find_target != -1:
    print(f'target find at {find_target}')
else:
    print(f'target not found')
    
names= array.array('u',['m','r'])
print(names)

# print('-----------',end)

number= array.array('i',[1,2,3,4,5,6,7,8,9,10])


def reverse(l):
    start = 0
    end=len(l)-1
    while start <=end:
        l[start],l[end]=l[end],l[start]
        print(l)
        start+=1
        end-=1
    return l

reversed=reverse(number)
print(reversed)