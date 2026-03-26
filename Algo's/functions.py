# def printHello():
#     print("hello User")
    
    
# printHello()

# finding minimum of two

# def minOfTwo(a,b):
#     if a>b:
#         return b
#     else:
#         return a

# def minOfTwo(a,b):
#     return a if a<b else b
# print(minOfTwo(100,450))

# def add(b,a,*args):
#     sum = a+b
#     for val in args:
#         sum+= val
#     return sum

# addi=add(10,20)
# print(addi)

# /sum of 1 to N

# def sumN(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum+=i
#     return sum

# print(sumN(3))

# n Factorial

# def facN(n):
#     fac=1
#     for i in range(1,n+1):
#         fac*=i
#     return fac
    
# print(facN(15))

# def add(a,b):
#     return a+b
# print(add)
# print(type(add))


#sum of digits in a number

# n=154
# sum = 0

# while n>0:
#     val=n%10
#     sum+=val
#     n=n//10
# print(sum)

# def sumOfDigit(n):
#     total=0
#     while n>0:
#         digit=n%10
#         total+=digit
#         n=n//10
#     return total

# print(sumOfDigit(1234506789))


# calculating nCr

def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

# print(factorial(10))

def nCr(n,r):
    factn=factorial(n)
    factr=factorial(r)
    factnmr=factorial(n-r)
    
    return factn/(factr *factnmr)

# print(nCr(6,3))

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

# print(isPrime(7))
# print(isPrime(11))

# print(int(29**0.5))

def prime(n):
    for num in range(2,n+1):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num%2==0:
                is_prime=False
                break
        if is_prime:
            print(num,end=" ")
            
# print(prime(25))

# fibonachi series

def febonachi(n):
    if n==0:
        return 'invalid numer'
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        a,b=0,1
        for _ in range(3,n+1):
            a,b=b,a+b
    return b

# print nth fibonacci

print(febonachi(10))