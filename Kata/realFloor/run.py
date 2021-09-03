def floor():
    floorNum = int(input("Enter floor number in American System\n"))
    if floorNum >= 1 and floorNum <=12:
        euroFlo0r = floorNum - 1
        print('-'*10)
        print('\n')
        print(f"Your Floor Number in Europe is {euroFlo0r}")
    elif floorNum >13:
        euroFlo0r = floorNum - 2 
        print('-'*10)
        print('\n')
        print(f"Your Floor Number in Europe is {euroFlo0r}")
    elif floorNum == 0:
        euroFlo0r = 0
        print('-'*10)
        print('\n')
        print(f"Your Floor Number in Europe is {euroFlo0r}")
    elif floorNum < 0:
        euroFlo0r = floorNum
        print('-'*10)
        print('\n')
        print(f"Your Floor Number in Europe is {euroFlo0r}")
    else:
        print('-'*10)
        print('\n')
        print("There is no 13th floor in America13")
floor()