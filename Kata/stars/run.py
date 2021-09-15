def stars():
    num = int(input("Enter a number\t"))
    #loop to handle number of rows which is num
    for i in range(0, num):
        #loop to handle number of column
        for j in range(0, i + 1):
            #print stars in a line
           print("*",end='')
           #end line after each row
        print('\n')
stars()


# def stars():
#     num = int(input("Enter a number\t"))
#     myList = []

#     for i in range(1,num+1):
#         myList.append('*'*i)
#     print('\n'.join(myList))
# stars()
