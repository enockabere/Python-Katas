def odd_even():
    num = int (input('Enter number to find whether odd/even\n'))
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')
odd_even()