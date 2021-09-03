#Reverse a string
def reverse_string():
    print("-"*5,'We\'re about to reverse a string','-'*5,'\n')
    
    '''
    declare a variable to store a string to be reversed
    and split the string into words
    '''
    
    mystring = input("Enter Sentence to Reverse\n")
    
    #check whether string entered is a sentence
    if ' ' in mystring:
        correct = mystring.split(' ')
    
        #reverse and join using space    
        mystring_reverse = ' '.join(reversed(correct))
    
        print ('*'*2,'Reversed String','*'*2,'\n',mystring_reverse)
    else:
        print("Invalid string! It should be a sentence")
reverse_string()



#reverse characters in string
def reverse_string():
    print("-"*5,'We\'re about to reverse a string','-'*5,'\n')
    
    '''
    declare a variable to store a string to be reversed
    and split the string into words
    '''
    
    mystring = input("Enter Sentence to Reverse\n").strip(' ')
    
    #reverse and join using space    
    mystring_reverse = ' '.join(reversed(mystring))
    
    print ('*'*2,'Reversed String','*'*2,'\n',mystring_reverse)
reverse_string()