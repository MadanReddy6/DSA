
def ValidAnagram(s, t):
    
    if len(s) != len(t):
        return False
    
    s1 = ''.join(sorted(s))
    t1 = ''.join(sorted(t))
    
    if s1 == t1:
        return True
    else:
        return False
    
print(ValidAnagram("racecar","carrace")) #True
print(ValidAnagram("racecar","carracee")) #False
