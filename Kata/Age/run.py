def main():
    age = input("Enter string that start with an integer\n").strip(" ")
    for i in age:
        if i.isdigit():
           myAge = int(i) 
           if myAge >=0 and myAge<=9:
               print(f'I\'m {myAge} years old')
           else:
               ("Not a child!")
        else:
            ("There is no integer in your input")
main()