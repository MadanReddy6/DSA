

def isValid(books , students , maxAllowedPages):
    student=1
    total_pages = 0
    
    for pages in books:
        if pages>maxAllowedPages:
            return False

        if total_pages+pages>maxAllowedPages:
            student+=1
            total_pages=pages
            if student>students:
                return False
        else:
            total_pages+=pages
    return True


def allocateBooks(books , students):
    if students > len(books):
        return False
    
    st = 0
    end = sum(books)
    result = -1
    
    while st <= end :
        mid = (st+end)//2
        
        if isValid(books,students,mid):
            result=mid
            end = mid-1
        else:
            st= mid+1
            
    return result
        
        
books = [10, 20, 30, 40]
students = 2

alloc=allocateBooks(books,students)
print(alloc)  