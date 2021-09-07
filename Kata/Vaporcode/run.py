def Vapor():
    vaporString = input("Enter String:-\n")
    
    #check if string is uppercase
    
    if vaporString.isupper():
        result="  ".join(vaporString)
        
    #else turn string to uppercase
    else:
        vaporString.upper()
        result="  ".join(vaporString)
    print("*"*5, 'Vaporwave Sentence',"*"*5,"\n", result )
Vapor()