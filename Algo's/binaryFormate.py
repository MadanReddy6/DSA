# converting binary to decimal numbers


def binToDecimal(binNum ):
    ans = 0
    pow = 1
    while binNum>0:
        rem = binNum%10
        ans +=rem*pow
        binNum //=10
        pow*=2
        
    return ans

print(binToDecimal(111001))