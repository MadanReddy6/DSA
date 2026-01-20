
class encode:
    
    def encodeDecodeString(self , liststr):
        self.liststr = liststr
        specialCharacter = '#'
        encoded =""
        
        for i in range(len(liststr)):
            encoded += liststr[i] + specialCharacter
        encoded = encoded[ : -1]
        return encoded 
        
    def decodeString(self, encoded):
        return encoded.split( '#')

obj = encode()
print(obj)
encode = obj.encodeDecodeString(['ad','b','cda','s'])
print(encode)
decode = obj.decodeString(encode)
print(decode)