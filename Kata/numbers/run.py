def numbers():
    numList = []
    num1=int(input("Enter num1\n"))
    num2=int(input("Enter num2\n"))
    num3=int(input("Enter num3\n"))
    
    numList.append(num1)
    numList.append(num2)
    numList.append(num3)
    
    newList=sorted(numList)
    for x in newList:
        if x % 4 == 0:
            print ('Woow!',x,'is a multiple of 4','*'*4)
    print('*'*4,newList.pop(),"IS THE LARGEST",'*'*4)
numbers()
    