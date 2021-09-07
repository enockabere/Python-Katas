#sorting and referencing data at list locations
def sortNum():
    mylist = [7,20,1,2,3,4,5]
    
    sortList = sorted(mylist)
    
    print('Smallest Number = \t',sortList[0],'\n','Lagest Number = \t',sortList.pop())
sortNum()
#sorting and referencing data at list locations using pop() method
def sortNum():
    mylist = [7,20,1,2,3,4,5]
    
    sortList = sorted(mylist)
    
    print('Smallest Number = \t',sortList[0],'\n','Lagest Number = \t',sortList[-1])
sortNum()
#using min and max iterables to find smallest and largest integer
def sortNum():
    mylist = [7,20,1,2,3,4,5]
    
    print('Smallest Number = \t',min(mylist),'\n','Lagest Number = \t',max(mylist))
sortNum()