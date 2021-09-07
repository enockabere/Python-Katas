def listTostring():
    mylist=['hello','world']
    
    result = " ".join(mylist)
    
    print(result)
listTostring()

#example to make a string a list and make it a string again

def listTostring():
    
    raw = input("Enter a list of words\n")
    
    #change string to list using split method
    result = list(raw.split(" "))
    
    #change list to string
    result2 = " ".join(result)
    
    print('*'*5,result ,'*'*2, 'CHANGED TO','*'*5,'\n',result2)
listTostring()
    
    
    