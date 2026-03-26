arr=[0,3,8,9,5,2,10,1]


# for i in range(1, len(arr) - 1):
#     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#         print(i)

# n = len(arr)
# for i in range(1, n - 1):
#     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#         print('--',i) 
        
        
        
        
        
# peak index in mountain array

def peak(l):
    n=len(l)
    for i in range(1,n-1):
        if l[i]>l[i-1] and l[i] > l[i+1]:
            return i
        
res=peak(arr)
print(res)