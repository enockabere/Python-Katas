def mulTable():
    y = list(range(1,11))
    s =int(input("Enter number to check its multiples\n"))
    for x in y:
        z = x*s
        print(f"{x}*{s}={z}")
mulTable()