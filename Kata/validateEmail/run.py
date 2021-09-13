def email():
    address= input("Enter email address to validate\n")
    x = list(address)
    
    if "@" in x and "." in x:
        print('*'*2,address, 'is valid','*'*2)
    else:
        print('*'*2,address, 'is invalid','*'*2)
email()