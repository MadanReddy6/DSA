arr=[2,0,2,1,1,0,1,2,0,0]
arr.sort()
print(arr)
arr = [2, 0, 2, 1, 1, 0, 1, 2, 0, 0]

# Count occurrences
count0 = 0
count1 = 0
count2 = 0

for i in arr:
    if i == 0:
        count0 += 1
    elif i == 1:
        count1 += 1
    else:
        count2 += 1

# Overwrite array with sorted order based on counts
index = 0

for i in range(count0):
    arr[index] = 0
    index += 1

for i in range(count1):
    arr[index] = 1
    index += 1

for i in range(count2):
    arr[index] = 2
    index += 1

print(arr)

# dutch national flag algo


arr = [2, 0, 2, 1, 1, 0, 1, 2, 0, 0]

def sortUsingDNF(l):
    low=0
    mid=0
    high=len(l)-1
    
    while mid<high:
        if  l[mid]==0:
            l[mid],l[low]=l[low],l[mid]
            mid+=1
            low+=1
        elif l[mid]==1:
            mid+=1
        else:
            l[mid],l[high]=l[high],l[mid]
            high-=1
            
    return l

res=sortUsingDNF(arr)
print(f"sort using DNF alog{res}")
